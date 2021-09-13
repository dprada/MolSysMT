import numpy as np

def get_sequence_identity(molecular_system, selection='all', reference_molecular_system=None,
                          reference_selection='all', syntaxis='MolSysMT', engine='biopython'):

    from molsysmt.topology.get_sequence_alignment import get_sequence_alignment

    if engine=='biopython':

        # This is code from ensembler.modeling.calculate_seq_identity
        # This should be implemented here importing the function but there is a conflict installing
        # ensembler: ensembler is only available for python 2.7
        # (https://github.com/choderalab/ensembler/blob/master/ensembler/modeling.py)

        group_indices = msm.select(molecular_system, target='group', selection=selection)
        reference_group_indices = msm.select(reference_molecular_system, target='group', selection=reference_selection)

        seq, seq_ref = get_sequence_alignment(molecular_system, selection=selection,
                reference_molecular_system=reference_molecular_system,
                reference_selection=reference_selection, syntaxis=syntaxis, engine=engine)

        intersect=[]
        intersect_ref=[]

        ii=0
        ii_ref=0

        for res, res_ref in zip(seq, seq_ref)

            if res!='-' and res_ref=='-':
                ii+=1
            elif res=='-' and res_ref!='-':
                ii_ref+=1
            elif res==res_ref:
                if res!='-' and res_ref!='-':
                    intersect_1.append(group_indices[ii])
                    intersect_2.append(reference_group_indices[ii_ref])
                    ii+=1
                    ii_ref+=1

        seq_id = 100 * float(seq_id) / float(len_shorter_seq)

        return identity, intersect, reference_intersect

    else:

        raise NotImplementedError

