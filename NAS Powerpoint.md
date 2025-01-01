## Types of NAS infastructure

### Custom
#### Pros
- Low cost (can be any computer)
- Upgradable (CPU, RAM, STORAGE, etc)
- Can run other services on it (Like plex [self hosted netflix], pi-hole [network wide bulletproof ad blocker] or homeassistant [smart home software])
- You'll end up actually learning how to set it up and diagnose problems when (not 'if') they occur.   
- More flexibility 
#### Cons
- Harder setup (takes roughly 3-4 hours to fully set up)
- You'll end up like these fucking nerds 
	"I ended up with like 80 terrabytes for only like, 1000 bucks"
	![[Pasted image 20241226102119.png]]
### Prebuilt
#### Pros
- Comes with SATA and stuff by default
- Lower power usage by 'out the box'
- Can more easily add drives (however there is still configuration when you do add them)
- Usually more robust 

#### Cons
- Can literally be a chromebook CPU with a fuck tonne of SATA ports
- Not Upgradable at all (most of the time)
- Higher cost 

## RAID
### What is RAID?
RAID (Redundant Array of Independent Disks) is a storage system that combines multiple drives in a number of possible configurations to improve performance and redundancy 
### Pros
- Splitting load between drives (like putting power supply in parallel to get more current)
- Redundancy for drive failures
![[Pasted image 20241226103904.png]]
### Cons
- Requires multiple drives, which can be most costly than a single higher capacity drive
- Higher power consumption as multiple drives are all on and spinning throughout any given write event. Also more drives = more power
## NAS Software
https://www.youtube.com/watch?v=hbVbFCVk2Bg
### What Software is available 
Generally pre built nas devices are designed specifically for the hardware.

When building a custom NAS, you'll have to choose your software yourself and set it up.




#### TrueNAS
- Literally has an app store
- Requires more ram
- Cannot expand without expanding by the same amount
	- e.g. If you have 2 drives you have to add another 2 of the same capacity
##
Other Things NAS can do 
- Outside of network access to files
- Simultaneous file access 
- backup files from your pc whenever they are both onj (syncthing)
- Block ads network wide automatically (pi hole)

#### Unraid
Better but expensive 
