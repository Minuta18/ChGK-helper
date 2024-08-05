import * as React from "react";

import "./flatButtonLink.css";

interface FlatButtonLinkProps {
    children?: React.ReactNode | React.ReactNode[];
    disabled?: boolean;
    href?: string;
}

export function FlatButtonLink(props: FlatButtonLinkProps) {
    return (
        <a 
            className="flat-button"
            href={ props.href }
        >
            { props.children }
        </a>
    );
}
