import * as React from "react";

import { IoWarning } from "react-icons/io5";

import { IconElement } from "../../iconElement";

interface WarningProps {
    show?: boolean;
    children?: React.ReactNode | React.ReactNode[];
}

export function Warning(props: WarningProps) {
    return (
        <IconElement className={ props.show ? "" : "hidden" } icon={
            <IoWarning size={24} color="#FD151B" />
        }>
            <span className="danger-text">
                { props.children }
            </span>
        </IconElement>
    );
}
