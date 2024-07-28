import React from "react";

import * as Kit from "../../../shared/kit";

export function NewsPanel() {
    return (
        <div>
            <Kit.Heading underlined={ false }>Новости</Kit.Heading>
            <Kit.News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены козлы" 
                link="http://sdohni.tvar" 
            />
            <Kit.News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены петухи" 
                link="http://sdohni.tvar" 
            />
            <Kit.News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены Степаны" 
                link="http://sdohni.tvar" 
            />
            <a href="/notifications" className="link">Уведомления</a>
        </div>
    );
}
