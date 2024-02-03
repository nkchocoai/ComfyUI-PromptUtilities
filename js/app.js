import { app } from "/scripts/app.js";
import { api } from "/scripts/api.js";

// refer. https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/Main/js/impact-pack.js
app.registerExtension({
    name: "Comfy.PromptUtilities.app",
    setup() {
        const refreshButton = document.getElementById('comfy-refresh-button');
        refreshButton.addEventListener('click', async function () {
            await fetch('/prompt_utilities/refresh', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({})
            }).then(response => { }).catch(error => {
                console.error('Error:', error);
            });
        });
    },
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === 'PromptUtilitiesFormatString' || nodeData.name === 'PromptUtilitiesJoinStringList') {
            let input_name = 'arg';
            let ignore_fields = ['prompt'];
            if (nodeData.name === 'PromptUtilitiesJoinStringList') {
                ignore_fields = ['separator'];
            }

            nodeType.prototype.onConnectionsChange = function (type, index, connected, link_info) {
                if (!link_info)
                    return;

                if (type == LiteGraph.OUTPUT) {
                    // connect output
                    if (connected && index == 0) {
                        if (this.outputs[0].type == '*') {
                            if (link_info.type == '*') {
                                app.graph._nodes_by_id[link_info.target_id].disconnectInput(link_info.target_slot);
                            }
                            else {
                                // propagate type
                                this.outputs[0].type = link_info.type;
                                this.outputs[0].label = link_info.type;
                                this.outputs[0].name = link_info.type;

                                for (let i in this.inputs) {
                                    let input_i = this.inputs[i];
                                    if (!ignore_fields.includes(input_i.name))
                                        input_i.type = link_info.type;
                                }
                            }
                        }
                    }

                    return;
                } else {
                    // connect input
                    if (ignore_fields.includes(this.inputs[index].name))
                        return;

                    if (this.inputs[0].type == '*') {
                        const node = app.graph.getNodeById(link_info.origin_id);
                        let origin_type = node.outputs[link_info.origin_slot].type;

                        if (origin_type == '*') {
                            this.disconnectInput(link_info.target_slot);
                            return;
                        }

                        for (let i in this.inputs) {
                            let input_i = this.inputs[i];
                            if (!ignore_fields.includes(input_i.name))
                                input_i.type = origin_type;
                        }

                        this.outputs[0].type = origin_type;
                        this.outputs[0].label = origin_type;
                        this.outputs[0].name = origin_type;
                    }
                }



                let converted_count = 0;
                for (const ignore_field of ignore_fields) {
                    let ignore_slot = this.inputs.find(x => x.name == ignore_field);
                    converted_count += ignore_slot ? 1 : 0;
                }

                if (!connected && (this.inputs.length > 1 + converted_count)) {
                    const stackTrace = new Error().stack;

                    if (
                        !stackTrace.includes('LGraphNode.prototype.connect') && // for touch device
                        !stackTrace.includes('LGraphNode.connect') && // for mouse device
                        !stackTrace.includes('loadGraphData') &&
                        !ignore_fields.includes(this.inputs[index].name)) {
                        this.removeInput(index);
                    }
                }

                let slot_i = 1;
                for (let i = 0; i < this.inputs.length; i++) {
                    let input_i = this.inputs[i];
                    if (!ignore_fields.includes(input_i.name)) {
                        input_i.name = `${input_name}${slot_i}`
                        slot_i++;
                    }
                }

                let last_slot = this.inputs[this.inputs.length - 1];
                if (
                    (ignore_fields.includes(last_slot.name) && this.inputs[this.inputs.length - 2].link != undefined)
                    || (!ignore_fields.includes(last_slot.name) && last_slot.link != undefined)) {
                    this.addInput(`${input_name}${slot_i}`, this.outputs[0].type);
                }
            }
        }
    },

    nodeCreated(node) {
        if (node.comfyClass == "PromptUtilitiesFormatString" || node.comfyClass == "PromptUtilitiesJoinStringList") {
            if (node.widgets) {
                node.widgets = node.widgets.filter(w => !node.inputs.some((input) => w.name === input.name));
            }
        }
    }
});

// refer. https://github.com/ltdrdata/ComfyUI-Impact-Pack/blob/Main/js/common.js
function nodeFeedbackHandler(event) {
    let nodes = app.graph._nodes_by_id;
    let node = nodes[event.detail.node_id];
    if (node) {
        const w = node.widgets.find((w) => event.detail.widget_name === w.name);
        if (w) {
            w.value = event.detail.value;
        }
    }
}

api.addEventListener("prompt-utilities-feedback", nodeFeedbackHandler);