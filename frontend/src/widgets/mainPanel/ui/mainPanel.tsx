import React from "react";

import "./mainPanel.css";

import * as Kit from "../../../shared/kit";

export function MainPanel() {
    return (
        <div>
            <Kit.Heading underlined={ false }>Недавнее</Kit.Heading>
            <Kit.GameShortcut 
                title="Турнир им. Стеапина" 
                numberOfQuestions={15}
                tags={[ 
                    <Kit.Tag color="#61E466">ЛЁГКИЙ</Kit.Tag>,
                    <Kit.Tag color="#6495ED">ТУРНИР</Kit.Tag>,
                ]} 
            />
            <Kit.GameShortcut 
                title="Треш от Стеапина" 
                numberOfQuestions={-2}
                tags={[ 
                    <Kit.Tag color="#CFCFCF">ПОЛЬЗОВАТЕЛЬСКИЙ</Kit.Tag>,
                ]} 
            />
            <Kit.GameShortcut 
                title="Вопросы про козлов" 
                numberOfQuestions={9} 
                tags={[ 
                    <Kit.Tag color="#E46161">СЛОЖНЫЙ</Kit.Tag>,
                ]} 
            />
            <Kit.Heading underlined={ false }>
                Стандартные пакеты вопросов
            </Kit.Heading>
            <Kit.GameShortcut 
                title="Все вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Kit.Tag color="#E2E461">СРЕДНИЙ</Kit.Tag>,
                ]} 
            />
            <Kit.GameShortcut 
                title="Лёгкие вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Kit.Tag color="#61E466">ЛЁГКИЙ</Kit.Tag>,
                ]} 
            />
            <Kit.GameShortcut 
                title="Нормальные вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Kit.Tag color="#E2E461">СРЕДНИЙ</Kit.Tag>,
                ]} 
            />
            <Kit.GameShortcut 
                title="Сложные вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Kit.Tag color="#E46161">СЛОЖНЫЙ</Kit.Tag>,
                ]} 
            />
        </div>
    );
}
