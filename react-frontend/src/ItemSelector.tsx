import React from 'react';

interface LeagueItem {
    name: string;
    url: string;
}

interface ItemSelectorProps {
    items: LeagueItem[];
    selectedItems: LeagueItem[]; 
    onItemClick: (item: LeagueItem) => void; 
}

const ItemSelector: React.FC<ItemSelectorProps> = ({ items, selectedItems, onItemClick }) => {
    return (
        <div id="itemGrid">
            {items.map((item) => (
                <div className="champIcon" key={item.name}>
                    <img
                        src={item.url}
                        onClick={() => onItemClick(item)} 
                        className={
                            selectedItems.some(i => i.name === item.name)
                                ? 'clicked'
                                : 'notClicked'
                        }
                        alt={item.name}
                    />
                </div>
            ))}
        </div>
    );
};

export default ItemSelector;