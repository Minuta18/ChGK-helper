import React from "react";
import { Link } from "react-router-dom";

import { MdOutlineAccountCircle } from "react-icons/md";
import { MdOutlineSettings } from "react-icons/md";
import { MdExitToApp } from "react-icons/md";
import { FaBars } from "react-icons/fa6";

import './header.css';

import { Logo } from "../../../shared/kit/logo/index";
import { Avatar } from "../../../shared/kit/avatar/index";
import { HeaderLink } from "../../../shared/kit/headerLink";
import { HoverDropdown } from "../../../shared/kit/hoverDropdown";
import { IconElement } from "../../../shared/kit/iconElement";

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
                    <span className="header__element hide-on-pc">
                        <HoverDropdown mainElement={ 
                            <FaBars 
                                color="var(--background-color)" 
                                size={ 40 }
                            /> 
                        }>
                            <Link to="/">Главная</Link>
                            <Link to="/play">Играть</Link>
                        </HoverDropdown>
                    </span>
                    <span className="header__element">
                        <HoverDropdown mainElement={ <Avatar /> }>
                            <IconElement icon={
                                <MdOutlineAccountCircle size={24}/>
                            }>
                                <Link to="/profile">Профиль</Link>
                            </IconElement>
                            <IconElement icon={
                                <MdOutlineSettings size={24}/>
                            }>
                                <Link to="/settings">Настройки</Link>
                            </IconElement>
                            <IconElement icon={
                                <MdExitToApp size={24} color="#FD151B"/>
                            }>
                                <Link to="/exit" className="danger-text">
                                    Выход
                                </Link>
                            </IconElement>
                        </HoverDropdown>
                    </span>
                    <span className="header__element hide-on-phones">
                        <HeaderLink to="/play">
                            Играть
                        </HeaderLink>
                    </span>
                    <span className="header__element hide-on-phones">
                        <HeaderLink to="/">
                            Главная
                        </HeaderLink>
                    </span>
                </div>
            </div>
        </nav>
    );
}