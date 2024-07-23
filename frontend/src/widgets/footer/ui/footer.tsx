import * as React from "react";
import { Logo } from "../../../shared/kit/logo/index";

import "./footer.css";

export function Footer() {
    return (
        <div className="footer">
            <div className="footer__inner">
                <div className="footer__column" style={{
                    alignItems: "center",
                }}>
                    <Logo />
                    © Джентльмены Кроковцы, 2024
                </div>
                <div className="footer__column" style={{
                    alignItems: "center",
                }}>
                    <a href="/policies/using-of-product">
                        Условия пользования продуктом
                    </a>
                    <a href="/policies/privacy-policy">
                        Политика конфиденциальности
                    </a>
                </div>
            </div>
        </div>
    );
}