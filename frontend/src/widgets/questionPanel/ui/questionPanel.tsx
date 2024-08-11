import * as React from "react";
import { IoIosSend } from "react-icons/io";

import "./questionPanel.css";

import * as Kit from "../../../shared/kit/index"

export function QuestionPanel() {
    return (
        <div>
            <Kit.Heading underlined={ false }>Вопрос #5</Kit.Heading>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In eu tristique diam. Nunc pulvinar luctus cursus. Donec eu mauris viverra, tempor leo eget, molestie massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam ullamcorper facilisis urna non facilisis. Suspendisse nisi nunc, ultrices et sagittis in, elementum vestibulum mi. Praesent sed dolor commodo, iaculis tortor a, tempor ex. Fusce sodales eros vel consequat varius. Vestibulum vel ante ac velit fringilla suscipit lacinia non metus. Donec nec sem id tortor dignissim mollis. Pellentesque et efficitur risus. Pellentesque eleifend, sem quis imperdiet hendrerit, sapien sapien commodo urna, in eleifend libero nibh sit amet orci. Curabitur porta nunc tellus, vel faucibus augue laoreet at. Ut erat ante, pellentesque et eleifend eget, molestie a turpis.</p>
            {/* <Kit.LoadingAnimation /> */}
            <form className="question-panel__form">
                <div className="question-panel__form-group">
                    <Kit.TextInput 
                        required={ true } placeholder="Ваш ответ"
                        name="question-field"
                    />
                    <Kit.IconButton>
                        <IoIosSend size={30} color="var(--white)" />
                    </Kit.IconButton>
                </div>
            </form>
            <br></br>
            <div className="correct-container">
                <div className="question-panel__auto-check">
                    <Kit.Heading underlined={ false }>
                        Автоматическая проверка
                    </Kit.Heading>
                    <Kit.Tag color="var(--tag-green)">ВЕРНО</Kit.Tag>
                </div>
                <p>
                Nulla dapibus ligula nisi, in lobortis turpis feugiat in. Sed tortor mi, lobortis in lobortis non, convallis et lorem. Sed eleifend pellentesque neque nec feugiat. Sed auctor pretium consectetur. Sed porttitor eget nisi nec aliquet. Nam in magna eu nulla feugiat faucibus a non felis. In leo nisi, commodo quis diam a, varius semper massa. Aliquam erat volutpat. Aenean quam velit, consectetur quis mi nec, efficitur faucibus nibh. In laoreet nisi et maximus consectetur. 
                </p>
                {/* <Kit.LoadingAnimation /> */}
            </div>
            <div className="question-panel__buttons-panel">
                <Kit.Button>
                    Следующий вопрос
                </Kit.Button>
                <Kit.FlatButton>
                    Завершить
                </Kit.FlatButton>
            </div>
        </div>
    );
}