import React from "react";
import { Link } from "react-router-dom";

import { MdOutlineAccountCircle } from "react-icons/md";
import { MdOutlineSettings } from "react-icons/md";
import { MdExitToApp } from "react-icons/md";
import { FaBars } from "react-icons/fa6";

import './header.css';

import * as Kit from "../../../shared/kit/index";

export function Header() {
    return (
        <nav className="header">
            <div className="header__inner">
                <div className="header__left">
                    <div className="header__element">
                        <Kit.Logo />
                    </div>
                </div>
                <div className="header__right">
                    <span className="header__element hide-on-pc">
                        <Kit.HoverDropdown mainElement={ 
                            <FaBars 
                                color="var(--background-color)" 
                                size={ 40 }
                            /> 
                        }>
                            <Link to="/">Главная</Link>
                            <Link to="/play">Играть</Link>
                        </Kit.HoverDropdown>
                    </span>
                    <span className="header__element">
                        <Kit.HoverDropdown mainElement={ <Kit.Avatar /> }>
                            <Kit.IconElement icon={
                                <MdOutlineAccountCircle size={24}/>
                            }>
                                <Link to="/profile">Профиль</Link>
                            </Kit.IconElement>
                            <Kit.IconElement icon={
                                <MdOutlineSettings size={24}/>
                            }>
                                <Link to="/settings">Настройки</Link>
                            </Kit.IconElement>
                            <Kit.IconElement icon={
                                <MdExitToApp size={24} color="#FD151B"/>
                            }>
                                <Link to="/exit" className="danger-text">
                                    Выход
                                </Link>
                            </Kit.IconElement>
                        </Kit.HoverDropdown>
                    </span>
                    <span className="header__element hide-on-phones">
                        <Kit.HeaderLink to="/play">
                            Играть
                        </Kit.HeaderLink>
                    </span>
                    <span className="header__element hide-on-phones">
                        <Kit.HeaderLink to="/">
                            Главная
                        </Kit.HeaderLink>
                    </span>
                </div>
            </div>
        </nav>
    );
}