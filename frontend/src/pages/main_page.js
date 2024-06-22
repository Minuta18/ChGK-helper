import { useCallback, useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton, SettingsButton,
} from '../ui/elements/buttons';

import * as api from '../api/api.js';

export default function MainPage() {
    const [isLoading, isInvalidToken, token] = api.tokens.useToken();

    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <SettingsButton />
                    <span className='header-text'>Добро пожаловать</span>
                    { isLoading ?
                        <p>Загрузка...</p>
                        :
                            isInvalidToken ?
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
