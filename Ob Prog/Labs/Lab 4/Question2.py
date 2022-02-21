
import random



class card:
    def __init__(self, suit, rank): 
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)
    

   




class Deck:
    
    def __init__(self,amount):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits =["Clubs", "Diamonds", "Hearts", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(card(suit, rank))
        
       
   
        
    def deck_total(self):
        return len(self.cards)
    
    def __str__(self):
        deck_total = self.deck_total()
        saying = f"I have shuffled a deck of {deck_total} cards"
        return saying

    def deal_card(self,amount):
        total = self.deck_total()

        for i in range(amount):
            print(self.cards[i])

            total = total -1
        print()
        print(f"There are {total} cards left")

        
    
    def shuffle(self):
        random.shuffle(self.cards)
        

       
def main():
    amount = 0
    hand = Deck(amount)
    print()
    print("Card Dealer")
    print()
    print(hand)
    print()
    print()
    
    
    amount = int(input("How many cards would you like?  "))
    print()
    hand = Deck(amount)
    
    hand.shuffle()
    hand.deal_card(amount)
    

if __name__ == "__main__":
    main()