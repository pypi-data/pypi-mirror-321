import argparse
import os
import string


def capitalize_underscore(text: str) -> str:
    text_list = list(text)
    text_list[0] = text[0].upper()
    for i in range(len(text_list)):
        if text_list[i] == '_' and i != len(text_list) - 1:
            text_list[i+1] = text_list[i+1].upper()
            
    while '_' in text_list:
        text_list.remove('_')

    return ''.join(text_list)


def main():
    parser = argparse.ArgumentParser(description="Maxcord-CLI")
    subparsers = parser.add_subparsers(
        title="Commands",
        dest="command",
        required=True,
        help="Available commands"
    )
    
    subparsers.add_parser(
        "create",
        help="Create the base folders and main.py"
    )
    
    make_parser = subparsers.add_parser(
        "make",
        help="Create a cog"
    )
    
    make_parser.add_argument(
        "name",
        help="Cog name"
    )
    
    args = parser.parse_args()
    file_path = os.path.realpath(os.path.dirname(__file__))
    
    match args.command:
        case "create":
            env = open(".env", 'w')
            env.write("BOT_TOKEN=")
            env.close()
            
            main = open("main.py", 'w')
            main_template = open(f"{file_path}/main_template.py", 'r').read()
            main.write(main_template)
            main.close()
            
            if not os.path.exists("cogs"):
                os.makedirs("cogs")
            
            print("Base discord bot created")

        case "make":
            if not os.path.exists("cogs"):
                os.makedirs("cogs")
            cog_template = open(f"{file_path}/cog_template.py", 'r').read()
            chaine = [char for char in args.name if char.upper() in string.ascii_uppercase or char == '_']
            cog_name = ''.join(chaine)
            cog_template = cog_template.replace("COG_NAME", capitalize_underscore(cog_name))
            cog = open(f"cogs/{args.name.lower()}_cog.py", 'w')
            cog.write(cog_template)
            cog.close()
            
            print("Cog created")

if __name__ == "__main__":
    main()
