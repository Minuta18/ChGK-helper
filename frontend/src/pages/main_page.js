import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

import * as api from '../api/api.js';

export default function MainPage() {
    console.log(api.tokens.checkToken());
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Добро пожаловать</span>
                    { !(api.tokens.checkToken()) ?
                        <>
                            <LinkButtonPrimary href='/auth/login'>
                                Вход
                            </LinkButtonPrimary>
                            <LinkButtonPrimary href='/auth/register'>
                                Регистрация
                            </LinkButtonPrimary>
                            <LinkButtonSecondary href='/game'>
                                Играть без регистрации
                            </LinkButtonSecondary>
                        </>
                        :
                        <>
                            <LinkButtonPrimary href='/game'>
                                Случайные вопросы
                            </LinkButtonPrimary>
                            <LinkButtonPrimary href='/game'>
                                Архив вопросов
                            </LinkButtonPrimary>
                        </>
                    }
                </Modal>
            </Background>
        </>
    );
}
