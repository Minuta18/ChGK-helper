import React from 'react';

import { 
    ButtonPrimary, ButtonSecondary,
} from '../ui/elements/buttons';

export default function IncorrectAnswer(props) {
    console.log(props);    
    return (
        <>
            <span className='header-text'>Ответ не верный</span>
            <span> { props.answer } </span>
            <span> { props.comment } </span>
            
            <ButtonPrimary disabled={ false } onClick={ props.onGo }>
                Далее
            </ButtonPrimary>
            <ButtonSecondary disabled={ false } onClick={ props.onEnd }>
                На главную
            </ButtonSecondary>
            <ButtonSecondary disabled={ false } onClick={ props.onGo2 }>
                Учитывать мой ответ как верный
            </ButtonSecondary>
        </>
    );
}
