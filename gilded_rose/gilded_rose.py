class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def check_item_quality_below_50(self, item):
        if item.quality < 50:
            item.quality += 1
    def check_item_quality_above_0(self, item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality -= 1

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.check_item_quality_above_0(item)
            else:
                self.check_item_quality_below_50(item)
                if item.name == "Backstage passes to a TAFKAL80ETC concert":
                    if item.sell_in < 11:
                        self.check_item_quality_below_50(item)
                    if item.sell_in < 6:
                        self.check_item_quality_below_50(item)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        self.check_item_quality_above_0(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self.check_item_quality_below_50(item)
