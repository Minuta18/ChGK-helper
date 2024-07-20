import React from "react";

import { Logo } from "../../../shared/kit/logo/index";
import { Avatar } from "../../../shared/kit/avatar/index";

import './header.css';

export function Header() {
    return (
        <nav className="header">
            <div className="header__inner">
                <div className="header__left">
                    <div className="header__element">
                        <Logo />
                    </div>
                </div>
                <div className="header__right">
                    <span className="header__element">
                        <Avatar />
                    </span>
                    <a href="/" className="header__element">
                        <span className="header__element-inner not-active">
                            Играть
                        </span>
                    </a>
                    <a href="/" className="header__element">
                        <span className="header__element-inner active">
                            Главная
                        </span>
                    </a>
                </div>
            </div>
        </nav>
    );
}