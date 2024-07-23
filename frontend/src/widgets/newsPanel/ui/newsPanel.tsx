import React from "react";

import { Heading } from "../../../shared/kit/heading/index";
import { News } from "../../../shared/kit/news/ui/news";

export function NewsPanel() {
    return (
        <div>
            <Heading underlined={ false }>Новости</Heading>
            <News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены козлы" 
                link="http://sdohni.tvar" 
            />
            <News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены петухи" 
                link="http://sdohni.tvar" 
            />
            <News 
                name="Релиз 236.382.1,2e29" 
                shortText="Добавлены Степаны" 
                link="http://sdohni.tvar" 
            />
            <a href="/notifications" className="link">Уведомления</a>
        </div>
    );
}
