import React from "react";

import "./logo.css";

import {ReactComponent as LogoSvg} from "./logo.svg";

export function Logo() {
    return (<div className="logo">
        <LogoSvg />
    </div>);
}
