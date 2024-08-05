import * as React from "react";
import { MdNumbers } from "react-icons/md";

import { IconElement } from "../../iconElement";
import { FaPlay } from "react-icons/fa";

import "./gameShortcut.css"

interface GameShortcutsProps {
    title: string;
    numberOfQuestions?: number;
    tags?: React.ReactNode[];
}

function getWordByNumber(number: number): string {
    if (number % 100 >= 11 && number % 100 <= 20) {
        return "ов";
    } else if (number % 10 === 1) {
        return "";
    } else if (number % 10 >= 2 && number % 10 <= 4) {
        return "а";
    } else if ((number % 10 >= 5 && number % 10 <= 9) || (number % 10 === 0)) {
        return "ов";
    }
    return "ов";
}

export function GameShortcut(props: GameShortcutsProps) {
    return (
        <div className="game-shortcut">
            <div className="game-shortcut__inner">
                <div className="game-shortcut__first-part">
                    <div className="game-shortcut__title">
                        <b>{ props.title }</b>
                        { props.tags?.map((tag, ind) => {
                            return <div key={ ind }>
                                { tag }
                            </div>
                        }) }
                    </div>
                    <div className="game-shortcut__stats">
                        { props.numberOfQuestions != null ?
                            <IconElement icon={ <MdNumbers /> }>
                                { props.numberOfQuestions } { 
                                    "вопрос" + getWordByNumber(
                                        props.numberOfQuestions
                                    ) 
                                }
                            </IconElement> :
                            ""
                        }
                    </div>
                </div>
                <div className="game-shortcut__second-part">
                    <FaPlay size={ 40 } className="game-shortcut__icon" />
                </div>
            </div>
        </div>
    );
}
