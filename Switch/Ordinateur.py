class Ordinateur:
    def __init__(self, addrIP, addrMAC, nomHote, tableARP, masqueSousReseau, defaultGateway):
        self.addrIP = addrIP
        self.addrMAC = addrMAC
        self.nomHote = nomHote
        self.tableARP = tableARP
        self.masqueSousReseau = masqueSousReseau
        self.defaultGateway = defaultGateway

    def sentTo(self, ordinateur):
        print("\n\n\n___________Simulation Commutateur (Switch)___________")
        print("\n\tOrdinateur source : " + str(self.nomHote) + " - " + str(self.addrIP))        
        print("\n\tOrdinateur destination : " + str(ordinateur.nomHote) + " - " + str(ordinateur.addrIP))      
        print("\n\nEtapes : ")
        print("\n\t-Demande " + str(self.nomHote) + " to " + str(ordinateur.nomHote))
        print("\n\t-Remplissage de la table ARP du " + str(self.nomHote))
        print("\n\t-Diffusion (Switch) ")
        print("\n\t-Remplissage de la table d'adresse MAC du Commutateur (Switch) ")
        print("\n\t-Reponse envoyée par la destination " + "(" + str(ordinateur.nomHote) + ")\n\n")
