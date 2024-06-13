import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function Correct_answer(props) {
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Ответ верный!</span>
                    <span> Правильный ответ: { props.answer } </span>
                    <span> Комментарий: { props.comment } </span>
                    <LinkButtonPrimary disabled={ false }>
                        Далее
                    </LinkButtonPrimary>

                    <LinkButtonSecondary disabled={ false }>
                        Отмена
                    </LinkButtonSecondary>

                    <LinkButtonSecondary disabled={ false }>
                        Нет мой ответ верный
                    </LinkButtonSecondary>
                    
                </Modal>
            </Background>
        </>
    );
}