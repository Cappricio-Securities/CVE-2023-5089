#!/usr/bin/env python

"""
 * CVE-2023-5089
 * CVE-2023-5089 Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */


"""
import getpass
username = getpass.getuser()


def display_help():
    help_banner = f"""

👋 Hey \033[96m{username}
   \033[92m                                                                          v1.0
   _______    ________    ___   ____ ___  _____       __________  ____  ____
  / ____/ |  / / ____/   |__ \ / __ \__ \|__  /      / ____/ __ \( __ )/ __ \\
 / /    | | / / __/________/ // / / /_/ / /_ <______/___ \/ / / / __  / /_/ /
/ /___  | |/ / /__/_____/ __// /_/ / __/___/ /_____/___/ / /_/ / /_/ /\__, /
\____/  |___/_____/    /____/\____/____/____/     /_____/\____/\____//____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mCVE-2023-5089 : Bug scanner for WebPentesters and Bugbounty Hunters

\x1b[31;1m$ \033[92mCVE-2023-5089\033[0m [option]

Usage: \033[92mCVE-2023-5089\033[0m [options]

Options:
  -u, --url     URL to scan                                CVE-2023-5089 -u https://target.com
  -i, --input   <filename> Read input from txt             CVE-2023-5089 -i target.txt
  -o, --output  <filename> Write output in txt file        CVE-2023-5089 -i target.txt -o output.txt
  -c, --chatid  Creating Telegram Notification             CVE-2023-5089 --chatid yourid
  -b, --blog    To Read about CVE-2023-5089 Bug            CVE-2023-5089 -b
  -h, --help    Help Menu
    """
    print(help_banner)


def banner():
    help_banner = f"""
    \033[94m
👋 Hey \033[96m{username}
      \033[92m                                                                      v1.0
   _______    ________    ___   ____ ___  _____       __________  ____  ____
  / ____/ |  / / ____/   |__ \ / __ \__ \|__  /      / ____/ __ \( __ )/ __ \\
 / /    | | / / __/________/ // / / /_/ / /_ <______/___ \/ / / / __  / /_/ /
/ /___  | |/ / /__/_____/ __// /_/ / __/___/ /_____/___/ / /_/ / /_/ /\__, /
\____/  |___/_____/    /____/\____/____/____/     /_____/\____/\____//____/

                              \033[0mDeveloped By \x1b[31;1m\033[4mhttps://cappriciosec.com\033[0m


\x1b[31;1mCVE-2023-5089 : Bug scanner for WebPentesters and Bugbounty Hunters

\033[0m"""
    print(help_banner)
