# Disclaimer
**This project is for educational purposes and I, the developer, am not responsible for who or what happens with this script.** This was mostly for cybersecurity research purposes on my end. 


# How to use
1) In the `Auto_Vote.py` you'll have to change this to `driver.get("<Your Voting page URL>")` with your URL to who you want to vote for the CampusTech giveaway. For the script to work correctly, you'll need to use a `https://campustech.org/tech-the-halls?entry_id=xxx` URL, you can get that URL by clicking the share button on whoever you want to spam vote. 
2) At the bottom of `Auto_Vote.py`, there's these couple lines, where it says `for _ in range(100)`, change the 100 to whatever number of instances you want to run. If you choose a high number like 100 and stop the script mid-way, the script will essentially be a virus and you'll see why if that happens to you, so don't stop the script mid-way. 
```python 
if __name__ == "__main__":
    processes = []
    for _ in range(100):
        p = multiprocessing.Process(target=vote)
        p.start()
        processes.append(p)
        time.sleep(random.randint(10, 600))
        for p in processes:
            p.join()
```  
3) Run `python install -r requirements.txt` or `py install -r requirements.txt` to install the dependencies
4) And then run `python Auto_Vote.py` or `py Auto_Vote.py` to run the script

*Should be easy to understand*
