import * as React from "react";

import "./textInput.css"

interface TextInputProps {
    disabled?: boolean;
    required?: boolean;
    placeholder?: string;
    name?: string;
    children?: React.ReactNode | React.ReactNode[];
    type?: string;
    reactFormStuff?: any; // idk what has this thing type
}

export function TextInput({ 
    disabled = false, required = false, placeholder, name = "fd", children,
    type = "text", reactFormStuff = null
} : TextInputProps) {
    return (
        (reactFormStuff !== null) ?
            <input 
                type={ type } disabled={ disabled } required={ required } 
                placeholder={ placeholder } name={ name } 
                className="text-input" { ...reactFormStuff }
            >
                { children }
            </input> : 
            <input 
                type={ type } disabled={ disabled } required={ required } 
                placeholder={ placeholder } name={ name } 
                className="text-input" 
            >
                { children }
            </input>
    );
}
