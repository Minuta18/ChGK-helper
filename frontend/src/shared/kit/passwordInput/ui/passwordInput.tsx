import * as React from "react";

import { BsFillEyeFill, BsFillEyeSlashFill } from "react-icons/bs";

import "./passwordInput.css"

interface PasswordInputProps {
    disabled?: boolean;
    required?: boolean;
    placeholder?: string;
    name?: string;
    children?: React.ReactNode | React.ReactNode[];
}

export function PasswordInput({ 
    disabled = false, required = false, placeholder, name, children,
} : PasswordInputProps) {
    const [ type, setType ] = React.useState<string>("password");

    return (
        <div className="password-input">
            <input 
                type={ type } disabled={ disabled } required={ required } 
                placeholder={ placeholder } name={ name } 
                className="password-input__input"
            >
                { children }
            </input>
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