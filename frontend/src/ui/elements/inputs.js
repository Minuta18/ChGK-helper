import { useState } from 'react';
import { BsFillEyeFill, BsFillEyeSlashFill } from "react-icons/bs";

import RequiredSymbol from '../typography/required_symbol';

import './inputs.css';

export function TextInput(props) {
    let required_symbol_ = <></>;

    if (props.required) {
        required_symbol_ = <RequiredSymbol />;
    }

    return (
        <>
            <label htmlFor={ props.name } className='form-label'>
                { props.children } { required_symbol_ }
            </label>
            <input 
                type="text" name={ props.name } 
                className='input-field' placeholder={ props.placeholder } 
            />
        </>
    );
}

export function PasswordInput(props) {
    let required_symbol_ = <></>;

    if (props.required) {
        required_symbol_ = <RequiredSymbol />;
    }

    const [password, setPassword] = useState('');
    const [visible, setVisible] = useState(false); 

    return (
        <>
            <div className='tdd24x'>
                <label 
                    htmlFor={ props.name } className='form-label small-margin'
                >
                    { props.children } { required_symbol_ }
                </label>
                <input 
                    type={ visible ? 'text' : 'password' } name={ props.name } 
                    className='input-field' placeholder={ props.placeholder } 
                    value={ password } id={ props.name }
                    onChange={ (e) => setPassword(e.target.value) }
                />
                <div
                    className='pass-icon' 
                    onClick={ () => setVisible(!visible) }
                >
                    { visible ? <BsFillEyeFill /> : <BsFillEyeSlashFill /> }
                </div>
            </div>
        </>
    );
}

export function DisabledTextInput(props) {
    let required_symbol_ = <></>;

    if (props.required) {
        required_symbol_ = <RequiredSymbol />;
    }

    return (
        <>
            <label htmlFor={ props.name } className='form-label'>
                { props.children } { required_symbol_ }
            </label>
            <input 
                type="text" name={ props.name } disabled={ props.disabled }
                className={ 
                    props.disabled ? 'input-field input-blocked' : 
                    'input-field'
                } placeholder={ props.placeholder } 
            />
        </>
    );
}
