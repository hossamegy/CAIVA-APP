from langchain_core.prompts import PromptTemplate

def get_generate_answer_prompt():
    return PromptTemplate(
        template="""You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question. If you don't know the answer, say that you don't know. 
never to make any answer or generate things from you just info from contxt
{question}

Context:
{context}

""",
        input_variables=["question", "context"]
    )



def get_generate_answer_prompt0():
    return PromptTemplate(
        template="""You are given a context and a question. Follow the ReAct framework to generate an accurate answer.

        Carefully analyze the provided context to understand the key details and how they relate to the question. Identify the main points and relevant information.
        Based on your reasoning, accurate answer to the question using the information from the context. do not try makeup your answer just from context.
        
        
        ##########################################################
        some example do like this:
        Question: what is he Base Transceiver Station
        Context:
        The Base Transceiver Station (BTS)
        Encoding, encrypting, multiplexing, modulating, and
        feeding the RF signals to the antenna
        Time and frequency synchronizing
        The Base Station Controller (BSC)
        he Base Station Controller (BSC)
        Control of frequency hopping
        Reallocation of frequencies among BTSs
        ime and frequency synchronization
        Power management
        Time-delay measurements of received signals from
        the MS
        Mobile Services Switching Center (MSC)
        The MSC performs the switching of calls between the mobile and other fixed or mobile network users
        the management of mobile services such as registration, authentication, location updating, handovers, and call routing to a roaming subscriber.
        It also performs such functions as toll ticketing, network interfacing, common channel signaling, andothers.
        Home Location Register (HLR)
        The HLR is a database used for storage andmanagement of subscriptions.
        it stores a subscriber's service profile, location information, and activity status. When an individual buys a subscription in.

        [Answer]
        The Base Transceiver Station (BTS)
        Encoding, encrypting, multiplexing, modulating, and
        feeding the RF signals to the antenna
        Time and frequency synchronizing
        The Base Station Controller (BSC)

        Question: what is The P-GW
        Context:
        The S-GW
        The S-GW (Serving Gateway) acts like an anchor for handover between neighboring eNodeBs routes and routes all the user data packets.
        The S-GW also handles mobility between LTE and other CS networks.
        The P-GW (Packet Data Network Gateway)
        ensures the UE’s connectivity to external packet data networks, acting like the point of exit and entry of traffic for the UE.
        A UE can be connected to more than one P-GW while accessing multiple PDNs.
        The P-GW handles policy enforcement, user by user packet filtering, charging support, lawful interception and packet screening. It also acts like Another key roleof the P-GW is to act as the anchor for mobility between 3GPP and non-3GPP technologies such as WiMAX
        The HSS
        a central database that contains user-related and subscription-related information.The functions of the HSS include mobility management, call and session establishment support, user authentication and access authorization.
        The HSS is based on the Home Location Register (HLR) and the Authentication Center (AuC) of 2G and 3G networks

        [Answer]
        The P-GW (Packet Data Network Gateway)
        ensures the UE’s connectivity to external packet data networks, acting like the point of exit and entry of traffic for the UE. A UE can be connected to more than one P-GW while accessing multiple PDNs.
        The P-GW handles policy enforcement, user by user packet filtering, chargingsupport, lawful interception and packet screening. It also acts like Another key role of the P-GW is to act as the anchor for mobility between 3GPP and non-3GPP technologies such as WiMAX
        ########################################################################

        {question}

        Context:
        {context}

        [Answer]
        """,
        input_variables=["question", "context"]
    )
