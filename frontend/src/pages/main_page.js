import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

export default function MainPage() {
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Добро пожаловать</span>
                    <LinkButtonPrimary href='/auth/login'>
                        Вход
                    </LinkButtonPrimary>
                    <LinkButtonPrimary href='/auth/register'>
                        Регистрация
                    </LinkButtonPrimary>
                    <LinkButtonSecondary href='/game'>
                        Играть без регистрации
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}
