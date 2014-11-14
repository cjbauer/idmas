Use Cases for a Deductive Reputation System
===========================================

A challenge for pseudonymous systems is to account for reputation.
One way to handle this is to assign trust numbers to participants and
have ways to adjust these trust numbers over time.  Here we consider a
very different possibility: the use of a deductive reputation systen
using a doxastic logic (modal logic of belief). The idea is that each
participant in the system can have their own beliefs about the state
of the world. If two participants have conflicting beliefs, then they
will not trust each other. A third party can still decide which of the
two (if either) to trust, but the system will make it impossible to
consistently trust both.

Here we give a few examples of how such a deductive reputation system
could be used.  We will use "Alice", "Bob" and "Carol" to refer to
participants in the system, though perhaps it is better to think of
these as referring to the public keys corresponding to the
pseudonyms. We will talk about Alice signing data, meaning the data
has been signed using the corresponding private key. All of this could
be generalised presumably to more elaborate notions of identity and to
multisignature possibilities, but we keep things simple to start.

Example 1: An Open Public IOU
-----------------------------

Suppose Alice has openly publicly agree to send Bob 1 bitcoin before
January 01, 2015.  This can be represented as a contract C which is
signed by both Alice and Bob. Since the contract is open, the signed
contract can be published to everyone.

On January 01, 2015, there are the following possibilities.

Case 1. Alice and Bob agree that Alice has paid Bob 1 bitcoin.
In this case, nothing more needs to happen. Third parties
can see that the contract expired and no conflict arose.

However, the following are possible:

Alice could sign and publish this proposition:

"Alice believes Alice paid Bob 1 bitcoin, fulfilling C."

Likewise Bob could sign and publish this proposition:

"Bob believes Alice paid Bob 1 bitcoin, fulfilling C."

In general, Alice can only sign and publish propositions of the form:

"Alice believes P."

Later if Carol wants to know if Alice is trustworthy, these published
propositions can be used as evidence.

Case 2. Suppose Alice has not paid Bob the 1 bitcoin. Here is what could happen:

Bob could sign and publish

"Bob believes Alice has not paid Bob 1 bitcoin as required by C. [expiration January 08, 2015]"

In this case the expiration date means that Bob's proposition is only
valid until January 08, 2015. This gives Alice a chance to respond.

If Alice does not respond, then Bob can republish the accusation
on January 08, 2015, with a later expiration date (or even with no expiration).
In this case, if Carol wants to know if Alice is trustworthy, Bob's published
accusation will be evidence she is not.

Alice could sign and publish a claim that she has paid Bob, but this
would probably mean little since she cannot provide a tx id from addresses
provably Alices and to addresses provably Bob's.

Case 3. Suppose Alice paid Bob the 1 bitcoin, but Bob accuses her of not having paid.

As in the previous case, Bob could sign and publish

"Bob believes Alice has not paid Bob 1 bitcoin as required by C. [expiration January 08, 2015]"

This time, Alice can respond by signing and publishing

"Alice believes Alice paid Bob 1 bitcoin as required by C in tx with id ID and output to Bob's address beta."

This would also need to include proof that the inputs were controlled
by Alice (which Alice can provide by additionally signing the
proposition with private keys for the input addresses to the
transaction) and, more importantly, that the address beta is
Bob's. This should be possible, but let us ignore these details here.

Now if Carol examines the state after Alice's published proposition
and before January 08, 2015, Carol will see both Bob's accusation and
Alice's response. It is not possible to consistently believe both that
Alice did not pay and that Alice did pay. Carol must distrust either
Bob or Alice. Alice's response should hold more weight since it
includes cryptographic evidence that she did pay, but ultimately the
decision of which to believe is up to Carol.

If Bob agrees that Alice has paid him after seeing her response (e.g.,
it was a misunderstanding on Bob's part), he should allow his
accusation to expire after January 08, 2015. After this, Carol could
consistently trust both Bob and Alice (or one or neither).

Example 2: A Closed Public IOU
------------------------------

This is a modification of the open public IOU in which the
fact that there was a contract is public, but the details
of the contract are not meant to be made public.
Here the contract C says

"Alice will send Bob 1 bitcoin before January 01, 2015.
Unless there is a dispute, these details are to remain private."

Alice and Bob can sign a hash of C and this signed hash can be published.

We again consider possibilities on January 01, 2015.

Case 1. Alice and Bob agree that Alice has paid Bob 1 bitcoin.
Alice and Bob might explicitly publish that each believes
the contract expired with no dispute, without giving details of
the contract.

It is also possible that, say, Alice signs and publishes the following:

"Alice believes Alice paid Bob 1 bitcoin, fulfilling C."

While this is true, it breaches the closed nature of the contract.
Bob could then sign and publish

"Bob believes Alice breached the terms of C by publishing its details."

The fact that Bob is correct is easily checkable by examining the terms
of C. Consequently, Carol could conclude that while Alice may be trusted
to pay her debts, she cannot be trusted to keep information private.

Case 2. Suppose Alice has not paid Bob the 1 bitcoin. There is a dispute which should
supersede the fact that the contract should remain closed. In this case,
Bob is allowed to openly sign and publish an accusation that Alice did not pay.
Since Alice did not pay, she cannot refute this accusation.

Case 3. Suppose Alice paid Bob the 1 bitcoin, but Bob accuses her of not having paid.
This proceeds as in the previous example. However, in this case it may permanently
damage Bob's reputation if he opens C (breaching C) when Alice has actually paid Bob.
Bob can avoid this damage by first signing and publishing:

"Bob believes Alice has breached hash(C). [expiration January 08, 2015]"

Alice can privately demonstrate to Bob that she has paid him and Bob will let the
accusation expire. Possibly Alice would want Bob to publish 

"Bob believes Alice has not breached hash(C)."

after January 08, 2015. (If Bob publishes it before, he has inconsistent published
beliefs, ruining his reputation.)

If Bob insists Alice has breached hash(C), Alice is allowed to open the details
of C and publish evidence that Alice paid Bob.

Example 3: A Private IOU
------------------------

This is like the previous case. However, neither party is allowed to
even publish that they have agreed to hash(C) unless there is a
dispute. Both have signed copies of C, so that if either one publishes
that there was an agreement, the other can publish C indicating that
there was a breach of C.

Example 4: A Fiat/Crypto Option
-------------------------------

We finally consider a more advanced example. Suppose the contract C is
a (European) call option Bob has purchased from Alice.

C: IF the bitcoin price is > 500 Euros on January 01, 2015, THEN
   IF Bob pays Alice 500 Euros by January 08, 2015, THEN
   Alice pays Bob 1 bitcoin by January 15, 2015.

Note that the final part of the contract is simply a version of the IOU
contract in the previous examples.

There are three interesting propositions here:

P1: The bitcoin price is > 500 Euros on January 01, 2015.
P2: Bob has paid Alice 500 Euros by January 08, 2015.
P3: Alice has paid Bob 1 bitcoin by January 15, 2015.

Claims about each of these propositions should not be published before
the relevant dates.

On January 02, 2015, both Alice and Bob should sign and publish
their determinations about P1. That is, Alice should sign and publish either

"Alice believes P1."
or
"Alice believes not P1."

Likewise for Bob. If either fails to sign and publish one of these statements,
then Carol could use this failure as evidence to distrust Alice or Bob.

Here there are several possibilities.

Case 1. If one of Alice or Bob believes P1 and the other believes not P1,
then there is a dispute. Carol can decide whether she believes P1 or
not P1 and use this to determine which of Alice or Bob she must
distrust.  Carol can probably reasonably determine whether or not P1
is true by looking up the bitcoin price from January 01, 2015.
However, there will always be some subjectivity here (especially
if the price is close to 500 Euros on January 01, 2015). If Carol does
not make this determination about P1, then she is still later allowed
to trust Alice or trust Bob, just not both at the same time.

Case 2. Alice and Bob agree that not P1. In this case, the contract
terminates and there is no dispute.

In the remaining cases Alice and Bob agree P1 and we must consider P2.
On January 09, 2015, both Alice and Bob should publish whether or not they
believe P2.

Case 3. Suppose Alice and Bob disagree about P2. (This almost certainly means
Bob says he paid and Alice says he didn't.) Here Carol would have little
evidence as to whether or not such a fiat transaction took place.
All Carol could realistically know is that one of Alice or Bob is untrustworthy.

Case 4. Suppose Alice and Bob agree on not P2: Bob did not pay.
Here the contract terminates and there is no dispute.

In the remaining cases Alice and Bob agree on P2 and we must consider P3.
At this point it is like the IOU in Example 1. Either both agree on P3
(Alice sent Bob 1 bitcoin) or Bob accuses Alice (Bob believes not P3).
If Bob accuses Alice, she either provides evidence or she does not.
