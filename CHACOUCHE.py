from tkinter import *
from tkinter import font

def validation():
    with open("fich.txt", "r") as file:
        lignes = file.readlines()
        informations = [ligne.strip().split(",") for ligne in lignes]
        mot_de_passe_entre = mot_de_passe_entry.get()
        for info in informations:
            if mot_de_passe_entre == info[0]:
                afficher_options(info[0], info[1], info[2], float(info[3]))
                return
        message.config(text="votre mot de passe est incorrect",fg="red")

def afficher_options(password, nom, prenom, solde):
    fenetre_options = Toplevel(fenetre_principale)
    fenetre_options.geometry("400x300")
    bouton_solde = Button(fenetre_options, text="Solde", command=lambda: afficher_solde(solde))
    bouton_retirer = Button(fenetre_options, text="Retirer", 
    )
    bouton_informations = Button(fenetre_options, text="Vos informations", command=lambda: infos(password, nom, prenom, solde))
    bouton_solde.place(x=150,y=100)
    bouton_retirer.place(x=250,y=30)
    
    bouton_informations.place(x=250,y=150)
def afficher_options(password, nom, prenom, solde):
    def retirer():
        nonlocal solde
        def retirer_solde():
            nonlocal solde
            montant = float(montant_entry.get())
            if montant > solde:
                msg =Label(fenetre_retirer)
                msg.config(text="Le montant demandé est supérieur à votre solde.", fg="red",font=("arial",8),bg="#14213D")
                msg.pack()
            else:
                solde -= montant
                msg1 =Label(fenetre_retirer)
                msg1.config(text=f"Retrait de {montant} Dhs effectué avec succès", fg="green",font=("arial",8),bg="#14213D")
                msg1.pack()
                #message.config(text=f"Retrait de {montant} Dhs effectué av Votre solde est maintenant de {solde} Dhs.", fg="green",font=("georgia",8))
                with open("fich.txt", "r") as file:
                    lignes = file.readlines()
                with open("fich.txt", "w") as file:
                    for ligne in lignes:
                        info = ligne.strip().split(",")
                        if info[0] == password:
                            info[3] = str(solde)
                            ligne = ",".join(info) + "\n"
                        file.write(ligne)

        fenetre_retirer = Toplevel()
        fenetre_retirer.geometry("320x200")
        fenetre_retirer.title("Retirer")
        fenetre_retirer.configure(bg="#14213D")

        Label(fenetre_retirer, text="Montant à retirer:",font=("Georgia",8,"bold","italic"),bd=3, relief="groove",background="#FCA311").place(x=20, y=50)
        montant_entry = Entry(fenetre_retirer,bd=3, relief="groove")
        montant_entry.place(x=170, y=50)

        valider_button = Button(fenetre_retirer, text="Valider", command=retirer_solde,font=("Georgia",8,"bold","italic"),bd=3, relief="groove",background="#FCA311")
        valider_button.place(x=80, y=100)

        quitter_button = Button(fenetre_retirer, text="Quitter", command=fenetre_retirer.destroy,font=("Georgia",8,"bold","italic"),bd=3, relief="groove",background="#FCA311")
        quitter_button.place(x=150, y=100)
        
    fenetre_options = Toplevel(fenetre_principale)
    fenetre_options.geometry("320x70")
    fenetre_options.configure(background="#14213D")
    fenetre_options.title("GESTION GAB")

    
    bouton_solde = Button(fenetre_options, text="Solde", command=lambda: afficher_solde(solde),background="#FCA311")
    bouton_retirer = Button(fenetre_options, text="Retirer", command=retirer,background="#FCA311")
    bouton_informations = Button(fenetre_options, text="Vos informations", command=lambda: infos(password, nom, prenom, solde),background="#FCA311")
    bouton_solde.place(x=50,y=20)
    bouton_retirer.place(x=250,y=20)
    bouton_informations.place(x=120,y=20)



def infos(password, nom, prenom, solde):
    fenetre_informations = Toplevel()
    fenetre_informations.title("vos informations")
    fenetre_informations.geometry("350x200")
    fenetre_informations.configure(background="#14213D")
    
    Label(fenetre_informations, text="Mot de passe:",width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=0, column=0, padx=10, pady=10)
    Label(fenetre_informations, text=password,width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=0, column=1, padx=10, pady=10)
    Label(fenetre_informations, text="Nom:",width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=1, column=0, padx=10, pady=10)
    Label(fenetre_informations, text=nom,width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=1, column=1, padx=10, pady=10)
    Label(fenetre_informations, text="Prenom:",width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=2, column=0, padx=10, pady=10)
    Label(fenetre_informations, text=prenom,width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=2, column=1, padx=10, pady=10)
    Label(fenetre_informations, text="Solde:",width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=3, column=0, padx=10, pady=10)
    Label(fenetre_informations, text=solde,width=15,font=("Georgia",10,"bold","italic"),bd=5, relief="groove",background="#FCA311").grid(row=3,column=1,padx=10,pady=10)

def afficher_solde(solde):
    fenetre_solde = Toplevel()
    fenetre_solde.geometry("300x200")
    fenetre_solde.title("Solde")
    fenetre_solde.configure(background="#14213D")

    Label(fenetre_solde,text=f"Votre solde est de :{solde} Dhs.",bg="#FCA311").place(x=50,y=80)

fenetre_principale = Tk()
fenetre_principale.title("GAB")
fenetre_principale.geometry("320x300")
fenetre_principale.configure(background="#14213D")
w = Label( fenetre_principale, text="Welcome to  RCA BANK",bg="#FCA311",width="300",height="3",font=("Giorgia",12,"italic" , "bold"),bd=5, relief="groove" )
w.pack()
saisir_mdp = Label(fenetre_principale,text="Entrer votre mot de passe:",fg="BLACK",bg="#FCA311",font=("Giorgia",10,"italic" , "bold"),bd=1, relief="groove")
saisir_mdp.pack()
saisir_mdp.place(x=80,y=100)
mot_de_passe_entry = Entry(fenetre_principale, show="*",bg="#E5E5E5",bd=3, relief="groove")
bouton_valider = Button(fenetre_principale,text="Valider",command=validation,bd=3, relief="groove",bg="#FCA311")
message = Label(fenetre_principale,fg="red",background="#14213D")

mot_de_passe_entry.place(x=95,y=130)
bouton_valider.place(x=135,y=170)
message.place(x=70,y=200)


fenetre_principale.mainloop()

