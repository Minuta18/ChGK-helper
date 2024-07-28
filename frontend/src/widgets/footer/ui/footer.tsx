import * as React from "react";
import * as Kit from "../../../shared/kit/index";

import "./footer.css";

export function Footer() {
    return (
        <div className="footer">
            <div className="footer__inner">
                <div className="footer__column" style={{
                    alignItems: "center",
                }}>
                    <Kit.Logo />
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