 # programe to convert the text to title form
 def titlecase (in_str) :
 	articles=['a','an','the','A','An','The']
 	conjuncts=['and','but','or','not','so','for','nor']
 	preps=['in','is','to','for','with','on','at','from','by','about','as','int','through','after','over','between','out','again','during','without','before','due to','under','around','among','of']
 	lowercase=articles+conjuncts+preps
 	out_str=""
 	in_list=in_str.split(" ")
 	out_str=in_list[0].capitalize() +" "
 	for word in in_list[l : ]:
 		if word in lowercase :
 			temp=word.lower()
 			out_str +=temp + " "
 		else:
 			temp=word.capitalize()
 			out_str +=temp + " "
 	return out_str
 line1=input("Enter the first line : ")
 line2=input("Enter the second line : ")
 print("\n\n")
 print(titlecase(line1))
 print(titlecase(line2))
 