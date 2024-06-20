import { useCallback, useEffect, useState } from 'react';
import { useCookies } from 'react-cookie';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

import * as api from '../api/api.js';

export default function MainPage() {
    const [loading, setLoading] = useState(true);
    const [invalidToken, setInvalidToken] = useState(true);
    const [cookie, setCookie, removeCookie] = useCookies(['auth-token']);

    const checkToken = useCallback(async (cookie) => {
        let result = await api.tokens.checkToken(cookie);
        console.log(result);
        // if (!result) removeCookie('auth-token');
        return result;
    }, []);

    useEffect(() => {
        checkToken(cookie['auth-token']).then((res) => { 
            setInvalidToken(!res); 
        });
        setLoading(false);
    }, []);

    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Добро пожаловать</span>
                    { loading ?
                        <p>Загрузка...</p>
                        :
                            invalidToken ?
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
