import { useState } from 'react';

import Timer from './timer.js';
import { DisabledTextInput } from './inputs.js';
import { ButtonPrimary } from './buttons.js';

import './question.css';

import * as api from '../../backend-lib/questions.js';

export function Question(props) {
    const [currTime, setCurrTime] = useState(1);
    const [disabled, setDisabled] = useState(true);
    
    let question = new api.Question(1);

    return (<>
        <div className='question__header'>
            <span className='header-text-but-smaller'>
                Вопрос #{ props.num }
            </span>
            {(currTime === 1) && <Timer initialTime={ props.tfr } onExpired={
                () => { setCurrTime(2);
            }} />}
            {(currTime === 2) && <Timer initialTime={ props.tfs } onExpired={
                () => { setCurrTime(3); setDisabled(false);
            }}/>}
            {(currTime === 3) && <Timer initialTime={ props.tft } 
            onExpired={() => {}} />}
        </div>
        <p className='full-width'>{ props.children }</p>
        <DisabledTextInput 
            name='answer' required={ true }
            placeholder='Ваш ответ' disabled={ disabled } 
        >
            Ответ
        </DisabledTextInput>
        <ButtonPrimary disabled={ disabled }>
            Проверить
        </ButtonPrimary>
    </>);
}
