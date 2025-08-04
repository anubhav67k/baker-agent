import React from "react";
import PanelRight from "@/coral/components/Panels/PanelRight";
import TaskDetails from "./TaskDetails";
import { TaskDetailsProps } from "@/models";

const PlanPanelRight: React.FC<TaskDetailsProps> = ({
    planData,
    loading,
    submittingChatDisableInput,
    OnApproveStep,
    processingSubtaskId
}) => {
    if (!planData) return null;

    return (
        <PanelRight
            panelWidth={350}
            defaultClosed={false}
            panelResize={true}
            panelType="first"
        >
            {planData.steps.map((step) => (
                <div key={step.id} className="plan-step" style={{ display: 'flex', alignItems: 'center', marginBottom: 8 }}>
                    {agentIcons[step.agent] || agentIcons['Human_Agent']}
                    <span style={{ marginLeft: 8 }}>{step.description}</span>
                    <span style={{ marginLeft: 16, fontSize: '0.9em', color: '#888' }}>Status: {step.status}</span>
                </div>
            ))}
            <div >
                <TaskDetails
                    planData={planData}
                    OnApproveStep={OnApproveStep}
                    submittingChatDisableInput={submittingChatDisableInput}
                    processingSubtaskId={processingSubtaskId}
                    loading={loading}
                />
            </div>
        </PanelRight>
    );
};

export default PlanPanelRight;
