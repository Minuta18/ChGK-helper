import * as React from "react";
import * as ReactRedux from "react-redux";

import * as Kit from "../../../shared/kit/index";
import * as Entities from "../../../entities/index";
import * as QuestionSlice from "../../../processes/questions/questionsSlice";

import "./questionList.css"

export function QuestionList() {
    const questionData = ReactRedux.useSelector(
        (state: any) => state.questions
    );
    const dispatch = ReactRedux.useDispatch<any>();

    return (
        <>
            <div className="question-list hide-on-pc">
                {
                    questionData.questions.map(
                        (object: any, ind: number) => {
                            if (object.status ===
                                Entities.QuestionStatus.SOLVED) {
                                return <Kit.RoundTag 
                                color="var(--tag-green)" key={ ind }>
                                    {ind + 1}
                                </Kit.RoundTag>;
                            } else if (object.status ===
                                Entities.QuestionStatus.FAILED) {
                                return <Kit.RoundTag 
                                color="var(--tag-red)" key={ ind }>
                                    {ind + 1}
                                </Kit.RoundTag>;
                            } else if (object.status ===
                                Entities.QuestionStatus.SKIPPED) {
                                return <Kit.RoundTag 
                                color="var(--tag-grey)" key={ ind }>
                                    {ind + 1}
                                </Kit.RoundTag>;
                            } else if (object.status ===
                                Entities.QuestionStatus.IN_PROGRESS) {
                                return <Kit.RoundTag 
                                    color="var(--primary-color)"
                                    key={ ind }
                                >
                                    {ind + 1}
                                </Kit.RoundTag>;
                            }
                            return <Kit.RoundTag color="var(--tag-grey)">
                                {ind + 1}
                            </Kit.RoundTag>;
                        }
                    )
                }
            </div>
            <div className="question-list hide-on-phones">
                {
                    questionData.questions.map(
                        (object: any, ind: number) => {
                            let status = "ok";
                            if (object.status === 
                                Entities.QuestionStatus.FAILED) {
                                status = "failed";
                            } else if (object.status === 
                                Entities.QuestionStatus.SKIPPED) {
                                status = "skipped";
                            } else if (object.status === 
                                Entities.QuestionStatus.IN_PROGRESS) {
                                status = "process";
                            }
                            return (
                                <Kit.Container key={ ind }>
                                    <Kit.Question 
                                        status={ status } onClick={() => {
                                            dispatch(
                                                QuestionSlice.selectQuestion(
                                                    ind
                                                )
                                            );
                                        }}>
                                        Вопрос #{ ind + 1 }
                                    </Kit.Question>
                                </Kit.Container>
                            );
                        }
                    )
                }
            </div>
        </>
    );
}
