import { useState, forwardRef, useRef, useCallback } from 'react';
import { BsFillEyeFill, BsFillEyeSlashFill } from "react-icons/bs";

import RequiredSymbol from '../typography/required_symbol';

import './inputs.css';

export const TextInput = forwardRef(
    function TextInput(props, ref) {
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
                    type="text" name={ props.name } ref={ ref } 
                    defaultValue={ props.defValue } className='input-field' 
                    placeholder={ props.placeholder } 
                />
            </>
        );
});

export const IntInput = forwardRef(
    function IntInput(props, ref) {
        let required_symbol_ = <></>;

        console.log('!', props.defValue);

        if (props.required) {
            required_symbol_ = <RequiredSymbol />;
        }

        return (
            <>
                <label htmlFor={ props.name } className='form-label'>
                    { props.children } { required_symbol_ }
                </label>
                {/* random key is used to force re-render of defaultValue */}
                <input 
                    type="number" name={ props.name } ref={ ref } 
                    defaultValue={ props.defValue } className='input-field' 
                    placeholder={ props.placeholder } 
                    key={"OKAYG_" + (10000 + Math.random() * (1000000 - 10000))}
                />
            </>
        );
});

export const PasswordInput = forwardRef(
    function PasswordInput(props, ref) {
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
                        htmlFor={ props.name } 
                        className='form-label small-margin'
                    >
                        { props.children } { required_symbol_ }
                    </label>
                    <input 
                        type={ visible ? 'text' : 'password' } 
                        name={ props.name } ref={ ref }
                        className='input-field' 
                        placeholder={ props.placeholder } 
                        defaultValue={ password } id={ props.name }
                        onChange={ (e) => setPassword(e.target.value) }
                    />
                    <div
                        className='pass-icon' 
                        onClick={ () => setVisible(!visible) }
                    >
                        { visible ? 
                            <BsFillEyeFill /> : 
                            <BsFillEyeSlashFill /> 
                        }
                    </div>
                </div>
            </>
        );
});

export const DisabledTextInput = forwardRef(
    function DisabledTextInput(props, ref) {
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
                    } placeholder={ props.placeholder } ref={ ref }
                />
            </>
        );
});
