import React from 'react';

import Background from '../ui/containers/background';
import Modal from '../ui/containers/modal';
import { TextInput, PasswordInput } from '../ui/elements/inputs';
import { 
    LinkButtonPrimary, LinkButtonSecondary, BackButton,
} from '../ui/elements/buttons';

import '../ui/elements/inputs.css';
import '../ui/elements/links.css';

export default function RegisterPage() {
    return (
        <>
            <Background>
                <Modal>
                    <BackButton />
                    <span className='header-text'>Регистрация</span>
                    <TextInput 
                        name='email' required={ true } 
                        placeholder='john@email.com'
                    >
                        Электронная почта
                    </TextInput>
                    <TextInput 
                        name='nickname' required={ true } 
                        placeholder='ExampleNickname'
                    >
                        Никнейм
                    </TextInput>
                    <PasswordInput 
                        name='password' required={ true }
                        placeholder='1234'
                    >
                        Пароль
                    </PasswordInput>
                    <PasswordInput 
                        name='password' required={ true }
                        placeholder='1234'
                    >
                        Подтверждение пароля
                    </PasswordInput>
                    <label class="form-label">
                        <input type="checkbox" class="input-checkbox" />
                        Я прочитал <a 
                            class="link"
                        >политику конфиденциальности</a> и <a 
                            class="link"
                        >условия пользования сервисом.</a>
                    </label>
                    <LinkButtonPrimary disabled={ false }>
                        Регистрация
                    </LinkButtonPrimary>
                    <LinkButtonSecondary href='/auth/login'>
                        У меня уже есть аккаунт
                    </LinkButtonSecondary>
                </Modal>
            </Background>
        </>
    );
}
