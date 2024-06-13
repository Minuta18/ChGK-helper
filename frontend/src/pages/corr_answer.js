import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function CorrectAnswer(props) {
    return (
        <>
            <span className='header-text'>Ответ верный</span>
            <span className='full-width'>
                { props.comment } 
            </span>
            <LinkButtonPrimary disabled={ false }>
                Далее
            </LinkButtonPrimary>
            <LinkButtonSecondary disabled={ false }>
                Отмена
            </LinkButtonSecondary>
        </>
    );
}