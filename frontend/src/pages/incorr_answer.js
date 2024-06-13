import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function IncorrectAnswer(props) {
    return (
        <>
            <span className='header-text'>Ответ не верный</span>
            <span> { props.answer } </span>
            <span> { props.comment } </span>
            <LinkButtonPrimary disabled={ false }>
                Далее
            </LinkButtonPrimary>
            <LinkButtonSecondary disabled={ false }>
                Отмена
            </LinkButtonSecondary>
            <LinkButtonSecondary disabled={ false }>
                Нет мой ответ верный
            </LinkButtonSecondary>
        </>
    );
}