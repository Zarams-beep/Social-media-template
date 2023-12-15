def addClass():
    selector = ['Mike','John','Kate','Blessing','Job','Thanks']
    while True:
        formerinfo = input('Enter former name: ').capitalize()

        # Keep prompting until a valid former name is provided
        while formerinfo not in selector:
            print(f'{formerinfo} not on the list. List remains unchanged.')
            formerinfo = input('Enter former name: ').capitalize()
        
        else: 
        # If a valid former name is provided, proceed to get the new name
            nowInfo = input('Enter new name: ').capitalize()
        
        #Update the list
            index = selector.index(formerinfo)
            selector[index] = nowInfo

        # Return a message with the former and new names, and the updated list
            print(f'Former name: {formerinfo}. New name: {nowInfo}. Updated list.' )
        
        response = input('Do you want to enter another new name? (y/n): ').lower()
        if response == 'y':
            continue
        elif response=='n':
            print(f'Thank you {nowInfo}. Enjoy the rest of your day!!')
            break
        else:
            print(f'Response: {response} is invaild. Ending!')
            break

addClass()