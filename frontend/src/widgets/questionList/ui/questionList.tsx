import * as React from "react";

import * as Kit from "../../../shared/kit/index";

import "./questionList.css"

export function QuestionList() {
    return (
        <>
            <div className="question-list hide-on-pc">
                <Kit.RoundTag color="#61E466">1</Kit.RoundTag>
                <Kit.RoundTag color="#E46161">2</Kit.RoundTag>
                <Kit.RoundTag color="#CFCFCF">3</Kit.RoundTag>
                <Kit.RoundTag color="#CFCFCF">4</Kit.RoundTag>
                <Kit.RoundTag color="#E46161">5</Kit.RoundTag>
            </div>
            <div className="question-list hide-on-phones">
                <Kit.Container>
                    <Kit.Question status="ok">
                        Вопрос #1
                    </Kit.Question>
                </Kit.Container>
                <Kit.Container>
                    <Kit.Question status="mistake">
                        Вопрос #2
                    </Kit.Question>
                </Kit.Container>
                <Kit.Container>
                    <Kit.Question status="skipped">
                        Вопрос #3
                    </Kit.Question>
                </Kit.Container>
                <Kit.Container>
                    <Kit.Question status="skipped">
                        Вопрос #4
                    </Kit.Question>
                </Kit.Container>
                <Kit.Container>
                    <Kit.Question status="mistake">
                        Вопрос #5
                    </Kit.Question>
                </Kit.Container>
            </div>
        </>
    );
}
