import { useRef, useState } from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput, PasswordInput } from '../ui/elements/inputs';
import { 
    ButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';
import { ErrorLabel } from '../ui/elements/labels';
import { redirect } from "react-router-dom";

import * as api from '../api/token';

export default function LoginPage() {
    let token = new api.AuthToken('');
    let user_password = useRef();
    let user_nickname = useRef();

    const [validNickname, setValidNickname] = useState(true);
    const [validPassword, setValidPassword] = useState(true);
    const [noErrors, setNoErrors] = useState(true);

    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Вход</span>
                    <TextInput 
                        name='nickname' required={ true } 
                        placeholder='ExampleNickname' ref={ user_nickname }
                    >
                        Никнейм или почта
                    </TextInput>
                    <ErrorLabel hidden={ validNickname }>
                        Никнейм не найден
                    </ErrorLabel>
                    <PasswordInput 
                        name='password' required={ true }
                        placeholder='1234' ref={ user_password }
                    >
                        Пароль
                    </PasswordInput>
                    <ErrorLabel hidden={ validPassword }>
                        Неверный пароль
                    </ErrorLabel>
                    <ErrorLabel hidden={ noErrors }>
                        Внутренняя ошибка сервера. Пожалуйста, сообщите о ней
                        здесь: 
                        <a 
                          href='https://github.com/Minuta18/ChGK-helper/issues'
                        >
                            https://github.com/Minuta18/ChGK-helper/issues
                        </a>
                    </ErrorLabel>
                    <ButtonPrimary onClick={() => {
                        setValidPassword(true);
                        setValidNickname(true);
                        token.fetchToken(
                            user_nickname.current.value, 
                            user_password.current.value,
                            () => { setValidPassword(false) },
                            () => { setValidNickname(false) },
                            () => { setNoErrors(false) },
                            () => { redirect('/home') },
                        );
                    }}>Вход</ButtonPrimary>
                    <LinkButtonSecondary href='/auth/register'>
                        Зарегистрироваться
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}
