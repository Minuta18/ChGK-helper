import React from "react";

import "./mainPanel.css";

import { Heading } from "../../../shared/kit/heading/index";
import { GameShortcut } from "../../../shared/kit/gameShortcut";
import { Tag } from "../../../shared/kit/tag/index";

export function MainPanel() {
    return (
        <div>
            <Heading underlined={ false }>Недавнее</Heading>
            <GameShortcut 
                title="Турнир им. Стеапина" 
                numberOfQuestions={15}
                tags={[ 
                    <Tag color="#61E466">ЛЁГКИЙ</Tag>,
                    <Tag color="#6495ED">ТУРНИР</Tag>,
                ]} 
            />
            <GameShortcut 
                title="Треш от Стеапина" 
                numberOfQuestions={-2}
                tags={[ 
                    <Tag color="#CFCFCF">ПОЛЬЗОВАТЕЛЬСКИЙ</Tag>,
                ]} 
            />
            <GameShortcut 
                title="Вопросы про козлов" 
                numberOfQuestions={9} 
                tags={[ 
                    <Tag color="#E46161">СЛОЖНЫЙ</Tag>,
                ]} 
            />
            <Heading underlined={ false }>Стандартные пакеты вопросов</Heading>
            <GameShortcut 
                title="Все вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Tag color="#E2E461">СРЕДНИЙ</Tag>,
                ]} 
            />
            <GameShortcut 
                title="Лёгкие вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Tag color="#61E466">ЛЁГКИЙ</Tag>,
                ]} 
            />
            <GameShortcut 
                title="Нормальные вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Tag color="#E2E461">СРЕДНИЙ</Tag>,
                ]} 
            />
            <GameShortcut 
                title="Сложные вопросы" 
                numberOfQuestions={15}
                tags={[ 
                    <Tag color="#E46161">СЛОЖНЫЙ</Tag>,
                ]} 
            />
        </div>
    );
}
