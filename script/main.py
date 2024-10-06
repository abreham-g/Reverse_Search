
import time
import random
import logging
import pandas as pd
from amazon_scraper import AmazonScraper

def main():
    """Main function to orchestrate the script execution."""
    scraper = AmazonScraper()

    products = [
    "Adeptus Mechanicus Sicarians Warhammer 40,000",
    "Games Workshop 99070101036 Dark Angels Primaris Upgrades Miniature",
    "Games Workshop - Warhammer 40,000 - Kill Team: Hand Of The Archon [video game]",
    "Games Workshop - Warhammer 40,000 - Leagues of Votann: Hearthkyn Warriors",
    "Games Workshop - 99120112043 - Warhammer 40,000 - Combat Patrol: Drukhari",
    "Warhammer 40,000: Space Marines - Tactical Squad",
    "GAMES WORKSHOP Warhammer 40k - Empire Tau Commander Shadowsun",
    "Warhammer Age of Sigmar - Kharadron Overlords Vanguard",
    "Games Workshop 99120206023 Skaven Pestilens Verminlord Corruptor Miniature",
    "Games Workshop - Warhammer 40,000 - Adepta Sororitas Penitent Engines/Engines of Redemption",
    "Games Workshop 99129915029 Warhammer Age of Sigmar Blue and Brimstone Horrors Action Figure",
    "Games Workshop - Middle Earth Strategy Battle Game: The Lord of The Rings - Isengard Battlehost",
    "Games Workshop Death Guard Daemon Primarch Mortarion Warhammer 40,000, 5 years to 99 years",
    "Games Workshop 99120102078 Death Guard Plague Marines Miniature, Black, 12 years to 99 years",
    "Games Workshop Warhammer 40k - Space Marine Primaris Invictor Tactical Warsuit 48-98 Black",
    "Warhammer 40,000: Adepta Sororitas Celestian Sacresants",
    "Games Workshop - Middle Earth Strategy Battle Game: The Lord of The Rings - Mordor Battlehost",
    "Warhammer Tau Empire Pathfinder Team 40,000",
    "Warhammer 40,000: Introductory Set",
    "Games Workshop - Warhammer 40,000 - Space Marines: Jump Pack Intercessors",
    "Warhammer Age of Sigmar Games Workshop Slaves to Darkness: Chaos Chosen",
    "Games Workshop Legion Cataphractii Terminator Squad",
    "Warhammer 40K Ultramarines Roboute Guilliman",
    "Games Workshop - Warhammer 40,000 - Chaos Space Marines Abaddon The Despoiler",
    "Space Marines Primaris Apothecary Warhammer 40,000",
    "Games Workshop Warhammer 40k - Space Marine Primaris Quad Invader",
    "Warhammer AoS - Sylvaneth Warsong Revenant",
    "Warhammer 40k - Genestealer Cults Neophyte Hybrids",
    "Games Workshop - Warhammer 40,000 - Aeldari: Rangers",
    "Games Workshop - Warhammer 40,000 - Leagues of Votann: Hernkyn Pioneers",
    "Games Workshop - Warhammer 40,000 - Adepta Sororitas: Aestred Thurga Relinquant at Arms",
    "Games Workshop Warhammer NECROMUNDA: PALANITE Enforcer Patrol",
    "Warhammer Games Workshop 40,000 - Chaos Space Marines Fabius Bile",
    "Games Workshop - Warhammer 40,000 - Kill Team: Legionaries",
    "Games Workshop - Warhammer 40,000 - Leagues of Votann: Grimnyr",
    "Ork Stormboyz Warhammer 40K Miniature Set",
    "Games Workshop - Warhammer 40,000 - Blood Angels: Death Company Intercessors",
    "Games Workshop 64-71 Warhammer Middle Earth - Fellowship of The Ring",
    "Warhammer 40,000: Tyranids - Lictor",
    "Combat Patrol Leagues of Votann Warhammer 40,000",
    "Games Workshop 99120218010 Start Collecting Stormcast Eternals Tabletop and Miniature Gaming, 12 years to 99 years",
    "Warhammer - Horus Heresy: CERASTUS Knight Acheron",
    "Warhammer 40,000: Necrons - Canoptek Spyder",
    "Games Workshop - Warhammer 40,000 - Leagues of Votann: The Ancestors Wrath",
    "Games Workshop - Warhammer 40,000 - Combat Patrol: Genestealer Cults",
    "Games Workshop - Warhammer 40,000 - Boarding Patrol: Adeptus Mechanicus",
    "Orks - Goff Rocker",
    "Warhammer 40,000: Necromunda - Gawdor Redemptionists",
    "Games Workshop - Warhammer 40,000 - Necrons Chronomancer",
    "Games Workshop Warhammer 40k - Grey Knights Castellan Crowe",
    "Games Workshop Warhammer 40k - Astra Militarum Lord Castellan Ursula Creed",
    "Games Workshop Warhammer 40k - Astra Militarum Solar Lord Leontus",
    "Games Workshop Warhammer 40k - Kill Team: Kasrkins",
    "Warhammer 40,000: Space Wolves Grey Hunters"
]


    results = []
    for product in products:
        link, asin = scraper.search_amazon(product)
        logging.info(f"Processed {product}: Link = {link}, ASIN = {asin}")
        results.append({
            "Title": product,
            "Amazon Link": link,
            "ASIN": asin
        })
        time.sleep(random.uniform(2, 5))  # Delay between requests

    df = pd.DataFrame(results)
    df.to_csv('../Data/amazon_product_links.csv', index=False)  

    # Close the Selenium WebDriver
    scraper.close_driver()

    print(df)
if __name__ == "__main__":
    main()