import * as React from "react";

import { BsFillEyeFill, BsFillEyeSlashFill } from "react-icons/bs";

import "./passwordInput.css"

interface PasswordInputProps {
    disabled?: boolean;
    required?: boolean;
    placeholder?: string;
    name?: string;
    children?: React.ReactNode | React.ReactNode[];
    reactFormStuff?: any; // see detailed description in textInput.tsx
}

export function PasswordInput({ 
    disabled = false, required = false, placeholder, name, children,
    reactFormStuff = null
} : PasswordInputProps) {
    const [ type, setType ] = React.useState<string>("password");

    return (
        <div className="password-input">
            { reactFormStuff !== null ?
                <input 
                    type={ type } disabled={ disabled } required={ required } 
                    placeholder={ placeholder } name={ name } 
                    className="password-input__input" { ...reactFormStuff }
                >
                    { children }
                </input> :
                <input 
                    type={ type } disabled={ disabled } required={ required } 
                    placeholder={ placeholder } name={ name } 
                    className="password-input__input"
                >
                    { children }
                </input>
            }
            <div className="password-input__icon" onClick={() => {
                if (type === "password") {
                    setType("text");
                } else {
                    setType("password");
                }
            }}>
                { type === "password" ?
                    <BsFillEyeFill /> :
                    <BsFillEyeSlashFill />
                }
            </div>
        </div>
    );
}