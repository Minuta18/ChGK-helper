import * as React from "react";

import "./textInput.css"

interface TextInputProps {
    disabled?: boolean;
    required?: boolean;
    placeholder?: string;
    name?: string;
    children?: React.ReactNode | React.ReactNode[];
    type?: string;
}

export function TextInput({ 
    disabled = false, required = false, placeholder, name, children,
    type = "text",
} : TextInputProps) {
    return (
        <input 
            type={ type } disabled={ disabled } required={ required } 
            placeholder={ placeholder } name={ name } className="text-input"
        >
            { children }
        </input>
    );
}
