
    
    
    
    subprocess.call( "mpc clear ", shell=True)
        subprocess.call( "mpc load snips.playlist.radio.txt ", shell=True)
        subprocess.call( "mpc  "+command, shell=True)
