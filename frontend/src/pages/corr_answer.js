import React from 'react';

import { 
    LinkButtonPrimary, LinkButtonSecondary,
} from '../ui/elements/buttons';

export default function CorrectAnswer(props) {
    return (
        <>
            <span className='header-text'>Ответ верный</span>
            <span className='full-width'>
                { props.comment } 
            </span>
            <LinkButtonPrimary onClick={ props.onClick }>
                Далее
            </LinkButtonPrimary>
            <LinkButtonSecondary onClick={ props.onEnd }>
                Отмена
            </LinkButtonSecondary>
        </>
    );
}