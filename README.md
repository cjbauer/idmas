Identity Management System based on BIP0032; runs in Tails Live OS.

"Digital pseudonyms, the creation of persistent network personas that
cannot be forged by others and yet which are unlinkable to the "true
names" of their owners, are finding major uses in ensuring free
speech, in allowing controversial opinions to be aired, and in
providing for economic transactions that cannot be blocked by local
governments. The technology being deployed by the Cypherpunks and
others, means their identities, nationalities, and even which
continents they are on are untraceable -- unless they choose to reveal
this information. This alters the conventional "relationship
topology" of the world, allowing diverse interactions without external
governmental refulation, taxation, or interference."

    Crypto Anarchy and Virtual Communities
    Timothy C. May in 1994

idmas is a free open source identity management system based on
BIP0032. Starting from a master seed, idmas can create a tree of
identities. Each of these identities has a profile: name, gender, age
and nationality. More importantly, each of these identities has an
extended private key corresponding to a node in the BIP0032
tree. Starting from this node the identity can deterministically
generate passwords and bitcoin private keys and addresses. It is also
easy to support other cryptocurrencies. Currently idmas can also
generate litecoin and darkcoin keys and addresses.

idmas is written in Python and is intended to be used in the
Tails live operating system (https://tails.boum.org).
Tails 1.1 (July 22, 2014) comes with Python 2.7.3 and this
is the only version of Python idmas has been tested using.
idmas does not use any extra Python modules not included with Tails.

* Quick Start

If you are using Tails, idmas should already work after you download
it. There are three executable Python scripts:

previewids : This is used when first planning your identity tree.
generateids : This is used to generate your identity tree.
idmas : This will be used on a regular basis after you have an identity tree.

You will need to add the idmas directory to your PATH, or give the path to the
executable scripts. I will assume the directory is in your PATH.

To see idmas in action quickly, try this:

previewids "not my secret"

The argument "not my secret" is the master seed used in this example.
The master seed you actually use should be random, should be kept
secret, and should never touch an online computer. By default
previewids generates a tree of breadth 2 and depth 2 (for a total of 6
identities). With the current values in config.py (which you can
adjust) this generates two Brazilian females, an American male, an
American female, a German male and a Mexican male.

Here is one of the six identities:

** Identity 1.1
Name: Caleb Jackie Davenport
Gender: Male
Nationality: American
Birthday: September 21, 1990
Age: 25
Cold:
priv 3UaUZ58oziqbX54DKVFz7w61iNXJTxef3JtZSao7R7uN 4ghepQqh8hGY8LbKLwBBxZSFisfphyUuVtaHr5yF3qfM
pub FLB8pr5v1bgcrKmr6NjdB6aYv2qedYBK5GCr4n8oPJ5a 3xamzBvZaXxuDRG9BDNNMzp8ZB4AvevCJ1y76XHdewvi 4ghepQqh8hGY8LbKLwBBxZSFisfphyUuVtaHr5yF3qfM
Warm:
priv E36bTaC1nkcS6gYuQUCGrdQejvdJR6r9zfTUbLmB8b9U B3Nbk4qz87eM2rG4a3L4eafRgoA84VNnL9Amhu96yuXK
pub 6imTsHamANi1xkZjjaUq5vDyiFyHAq36QzLhm6onyTTx HimhpJyTBxPHQHBHNu82MwgoxUqGLrZmTEUEX5UANDAk B3Nbk4qz87eM2rG4a3L4eafRgoA84VNnL9Amhu96yuXK
Hot:
priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy
pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy

More important than the profile information are the extended private
and public keys for certain "directory" nodes: cold, warm and
hot. These nodes can be used to generate passwords and cryptocoin keys
and addresses.

idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy passwords 0 5
idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy btc 7 3
idmas pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy btc 7 3
idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy ltc 2 2
idmas pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy ltc 2 2
idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy dash 2 2
idmas pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy dash 2 2
idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy nbt 2 2
idmas pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy nbt 2 2
idmas priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy clam 2 2
idmas pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy clam 2 2

At any later time you can use idmas offline to recover the identity
information from the master seed. In addition passwords are shown that
can be used to decrypt the hot and warm (online) directories. Here is
how to do this (offline, since it requires the master seed):

idmas master "not my secret" "1'/1'" identity

Name: Caleb Jackie Davenport
Gender: Male
Nationality: American
Birthday: September 21, 1990
Age: 25
* Cold:
priv 3UaUZ58oziqbX54DKVFz7w61iNXJTxef3JtZSao7R7uN 4ghepQqh8hGY8LbKLwBBxZSFisfphyUuVtaHr5yF3qfM
pub FLB8pr5v1bgcrKmr6NjdB6aYv2qedYBK5GCr4n8oPJ5a 3xamzBvZaXxuDRG9BDNNMzp8ZB4AvevCJ1y76XHdewvi 4ghepQqh8hGY8LbKLwBBxZSFisfphyUuVtaHr5yF3qfM
* Warm:
Pass: 9i48osHAxRMW9Nj
priv E36bTaC1nkcS6gYuQUCGrdQejvdJR6r9zfTUbLmB8b9U B3Nbk4qz87eM2rG4a3L4eafRgoA84VNnL9Amhu96yuXK
pub 6imTsHamANi1xkZjjaUq5vDyiFyHAq36QzLhm6onyTTx HimhpJyTBxPHQHBHNu82MwgoxUqGLrZmTEUEX5UANDAk B3Nbk4qz87eM2rG4a3L4eafRgoA84VNnL9Amhu96yuXK
* Hot:
Pass: RFHGP7rWthAVaiA
priv APWfWUopaDUxh6vdkrqciPnsDJAEk9h1T1mwuTxdyjzk CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy
pub 2JPuFHj26cYzBwSC9x5HmD5BWn2j6tLM6YvMGNzZefZz Aw6i9DQiH9jGzCjbicaRSffmzJrXwiwSfj64o1YkUAvY CgYFVTtBahpJpsF1gMJ75aKC74YLdfvJmZTRBNEGFmxy

Assuming we had a usb drive storing the encrypted hot and warm
directories, we could do something like the following in Tails:

cp /media/myusb/ids/1.1hot.tgz.gpg ~/

Then decrypt 1.1hot.tgz.gpg using the password RFHGP7rWthAVaiA and
untar the result as

tar xzvf 1.1hot.tgz

You can save persistent information in the directory 1.1hot.
1.1hot/info.txt will have information about how to use idmas to create
"hot" bitcoin private keys and addresses and "warm" bitcoin addresses
(where the private keys are only in 1.1warm). When you are finished
working as 1.1 (Caleb Davenport) and you want to save the data in
1.1hot, call the script 1.1hot/save. It will tar and gzip the file,
gpg encrypt it with the same password and copy it (along with a dated
backup of the previous version) to your usb storage directory
(/media/myusb/ids in this example).

Idmas can generate quite large identity trees. You call previewids
with a breadth of 4 and depth of 5 as:

previewids "not my secret" 4 5

The script with generate

  4^5 + 4^4 + 4^3 + 4^2 + 4 = 1364 identities.

That is probably more identities than you will ever use, but
the intention is that you have them generated and can easily bring
a new identity online.

* Preparing for Regular Use

When you are ready to start using idmas, copy it to an offline
computer running Tails. Your master seed should never touch an online
computer.

Before you seriously start using idmas you probably want to first
experiment with previewids while modifying the data in config.py.  The
data in config.py can be modified to affect the gender, nationalities
and ages of identities. For example, you may not wish to generate
identities for nationalities if you do not know the language.  In that
case, you can set those nationalities to 0. Also, if you want most of
your identities to be female, set gender_female to 9 and leave
gender_male set to 1.  Birthday lowerbounds and upperbounds can also
be adjusted.

After each adjustment call previewids and see if you are happy
with the current identity tree.

previewids "very strong random seed, seriously" 3 3

When you are happy with the mix of identity profiles, then
call generateids:

generateids "very strong random seed, seriously" /home/amnesia/darkids /media/myusb/dids 3 4

This will create the directory /home/amnesia/darkids. The hot and warm
directories for each identity will be created and gpg encrypted in
this directory /home/amnesia/darkids. The parameters 3 and 4 are the
breadth and depth of the tree, so in this case we are choosing to
generate 3^4+3^3+3^2+3 = 120 identities. The argument
"/media/myusb/dids" indicates where the hot and warm encrypted
directories will be stored (when online). generateids only uses it to
create the corresponding "save" scripts so you can easily save your
work later. You can modify the save scripts by hand later if you
change your persistent storage.

After the identities have been generated, copy the *gpg encrypted
versions to your persistent storage device. For example:

cd /home/amnesia/darkids
mkdir /media/myusb/dids
cp *gpg /media/myusb/dids/

* Regular Use

After all your identities have been generated, you can
work on your online computer as follows.

When you want to be identity 3.2, boot up with Tails and either copy
3.2hot.tgz.gpg (preferably) or 3.2warm.tgz.gpg (when necessary) to
your home directory. (The decrypted version should only be in RAM, not
on your usb storage device.)  Decrypt the file and expand the
directory. To decrypt the file you will, of course, need the
corresponding password. If it is an identity you are using often, you
will probably commit it to memory. Otherwise, go to your *offline*
computer and regenerate it:

idmas master "very strong random seed, seriously" "3'/2'" identity

While you are this identity you can use idmas to generate new passwords
and cryptocoin keys and addresses using the information in
3.2*/info.txt.

When you are finished working, save the directory using the save script.

* Relationship Topology

The tree structure can also act as a model of a relationship topology.
For example, the identity at node 1.1 ("1'/1'" in BIP0032) could be
considered "connected" to the identities at nodes 1, 1.2 and 1.1.x for
various values of x. Identities at nodes not connected to 1.1 should
never interact with it.

There are good arguments that two identities should never have a
connection:

"And then when you do your freedom fighting activities from your
online alias, when that gets compromised, the person that takes the
heat is your cover, someone who doesn’t exist. And it’s very critical
that you never contaminate. Contamination is when there is contact
between 2 cover identities or 2 aliases, or in this case between your
real identity and your cover persona. So be very conscious of
contamination – avoid it like the plague."

     The Grugq
   http://privacy-pc.com/articles/hackers-guide-to-stay-out-of-jail-2-dos-and-donts.html

However, contamination may be unavoidable in some cases, so it seems
prudent to have a policy like the one described above.

An example of unavoidable contamination is sending cryptocoins. You
should, of course, not have a single pool of coins every identity can
use. Each identity has his own addresses. In order for an identity to
obtain coins, he or she may obtain them from a connected identity.
Two identities without a direct connection should not be sending coins
to each other. For those with direct connections, it is still a good
idea to use mixers and coinjoin when sending coins.

* Code

Here is a guide to the code. It is all written in a functional style.
Excluding names.py (which is mostly a huge list of names), the total
code is less than 1000 lines.

crypto.py - This implements the Elliptic Curve secp256k1, base58
  encoding and BIP0032 operations.

config.py - This is a short configurable file you can adjust to your
  liking. It affects the profiles of generated identities.

names.py - This file is the largest because it mostly consists of
  first and last names classified by nationality and gender. The first
  few lines of the file define two helper functions addfirstname and
  addlastname. After that there are thousands of lines of the form
  addfirstname(...) and addlastname(...).

identity.py - This uses the code above to generate an identity
  profile.

idmas - This is the main executable script. It can be used to generate
  cryptocoin keys and addresses as well as passwords. The identity
  profile can also be obtained using either the master seed or the
  extended private key for the identity node. This script can also be
  used very generally to obtain BIP0032 descendents of extended
  private keys and extended public keys.

previewids - This is more or less a subset of generateids that does
  not create any directories or files. It is expected to be used while
  experimenting with the parameters in config.py before running
  generateids.

generateids - This will probably be called once before you start
  seriously using idmas. You can use it with your master seed to
  create a tree of identities along with corresponding gpg encrypted
  hot and warm directories.

* Authors

The code was written by Christian Bauer (based on other BIP0032
descriptions/implementations publicly available). Christian's PGP
public key should be included in the file cjbauer.asc.

This README text was largely written by Westin in collaboration with
Christian.
