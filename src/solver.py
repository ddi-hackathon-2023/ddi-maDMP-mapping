from dto import SSSOMOtherField


def cardinality_type_solver(of: SSSOMOtherField):
    solver ={
         ('0..1', 'list', '0..1', 'list'): 'convert_list',
         ('0..1', 'list', '0..1', 'literal'): 'convert_literal',
         ('0..1', 'list', '0..1', 'object'): 'convert_object',
         ('0..1', 'list', '0..1', 'voc'): 'convert_voc',
         ('0..1', 'list', '0..n', 'list'): 'convert_list',
         ('0..1', 'list', '0..n', 'literal'): 'convert_literal',
         ('0..1', 'list', '0..n', 'object'): 'convert_object',
         ('0..1', 'list', '0..n', 'voc'): 'convert_voc',
         ('0..1', 'list', '1', 'list'): 'convert_list',
         ('0..1', 'list', '1', 'literal'): 'convert_literal',
         ('0..1', 'list', '1', 'object'): 'convert_object',
         ('0..1', 'list', '1', 'voc'): 'convert_voc',
         ('0..1', 'list', '1..n', 'list'): 'convert_list',
         ('0..1', 'list', '1..n', 'literal'): 'convert_literal',
         ('0..1', 'list', '1..n', 'object'): 'convert_object',
         ('0..1', 'list', '1..n', 'voc'): 'convert_voc',
         ('0..1', 'list', 'n', 'list'): 'convert_list',
         ('0..1', 'list', 'n', 'literal'): 'convert_literal',
         ('0..1', 'list', 'n', 'object'): 'convert_object',
         ('0..1', 'list', 'n', 'voc'): 'convert_voc',
         ('0..1', 'literal', '0..1', 'list'): 'convert_list',
         ('0..1', 'literal', '0..1', 'literal'): 'convert_literal',
         ('0..1', 'literal', '0..1', 'object'): 'convert_object',
         ('0..1', 'literal', '0..1', 'voc'): 'convert_voc',
         ('0..1', 'literal', '0..n', 'list'): 'convert_list',
         ('0..1', 'literal', '0..n', 'literal'): 'convert_literal',
         ('0..1', 'literal', '0..n', 'object'): 'convert_object',
         ('0..1', 'literal', '0..n', 'voc'): 'convert_voc',
         ('0..1', 'literal', '1', 'list'): 'convert_list',
         ('0..1', 'literal', '1', 'literal'): 'convert_literal',
         ('0..1', 'literal', '1', 'object'): 'convert_object',
         ('0..1', 'literal', '1', 'voc'): 'convert_voc',
         ('0..1', 'literal', '1..n', 'list'): 'convert_list',
         ('0..1', 'literal', '1..n', 'literal'): 'convert_literal',
         ('0..1', 'literal', '1..n', 'object'): 'convert_object',
         ('0..1', 'literal', '1..n', 'voc'): 'convert_voc',
         ('0..1', 'literal', 'n', 'list'): 'convert_list',
         ('0..1', 'literal', 'n', 'literal'): 'convert_literal',
         ('0..1', 'literal', 'n', 'object'): 'convert_object',
         ('0..1', 'literal', 'n', 'voc'): 'convert_voc',
         ('0..1', 'object', '0..1', 'list'): 'convert_list',
         ('0..1', 'object', '0..1', 'literal'): 'convert_literal',
         ('0..1', 'object', '0..1', 'object'): 'convert_object',
         ('0..1', 'object', '0..1', 'voc'): 'convert_voc',
         ('0..1', 'object', '0..n', 'list'): 'convert_list',
         ('0..1', 'object', '0..n', 'literal'): 'convert_literal',
         ('0..1', 'object', '0..n', 'object'): 'convert_object',
         ('0..1', 'object', '0..n', 'voc'): 'convert_voc',
         ('0..1', 'object', '1', 'list'): 'convert_list',
         ('0..1', 'object', '1', 'literal'): 'convert_literal',
         ('0..1', 'object', '1', 'object'): 'convert_object',
         ('0..1', 'object', '1', 'voc'): 'convert_voc',
         ('0..1', 'object', '1..n', 'list'): 'convert_list',
         ('0..1', 'object', '1..n', 'literal'): 'convert_literal',
         ('0..1', 'object', '1..n', 'object'): 'convert_object',
         ('0..1', 'object', '1..n', 'voc'): 'convert_voc',
         ('0..1', 'object', 'n', 'list'): 'convert_list',
         ('0..1', 'object', 'n', 'literal'): 'convert_literal',
         ('0..1', 'object', 'n', 'object'): 'convert_object',
         ('0..1', 'object', 'n', 'voc'): 'convert_voc',
         ('0..1', 'voc', '0..1', 'list'): 'convert_list',
         ('0..1', 'voc', '0..1', 'literal'): 'convert_literal',
         ('0..1', 'voc', '0..1', 'object'): 'convert_object',
         ('0..1', 'voc', '0..1', 'voc'): 'convert_voc',
         ('0..1', 'voc', '0..n', 'list'): 'convert_list',
         ('0..1', 'voc', '0..n', 'literal'): 'convert_literal',
         ('0..1', 'voc', '0..n', 'object'): 'convert_object',
         ('0..1', 'voc', '0..n', 'voc'): 'convert_voc',
         ('0..1', 'voc', '1', 'list'): 'convert_list',
         ('0..1', 'voc', '1', 'literal'): 'convert_literal',
         ('0..1', 'voc', '1', 'object'): 'convert_object',
         ('0..1', 'voc', '1', 'voc'): 'convert_voc',
         ('0..1', 'voc', '1..n', 'list'): 'convert_list',
         ('0..1', 'voc', '1..n', 'literal'): 'convert_literal',
         ('0..1', 'voc', '1..n', 'object'): 'convert_object',
         ('0..1', 'voc', '1..n', 'voc'): 'convert_voc',
         ('0..1', 'voc', 'n', 'list'): 'convert_list',
         ('0..1', 'voc', 'n', 'literal'): 'convert_literal',
         ('0..1', 'voc', 'n', 'object'): 'convert_object',
         ('0..1', 'voc', 'n', 'voc'): 'convert_voc',
         ('0..n', 'list', '0..1', 'list'): 'convert_list',
         ('0..n', 'list', '0..1', 'literal'): 'convert_literal',
         ('0..n', 'list', '0..1', 'object'): 'convert_object',
         ('0..n', 'list', '0..1', 'voc'): 'convert_voc',
         ('0..n', 'list', '0..n', 'list'): 'convert_list',
         ('0..n', 'list', '0..n', 'literal'): 'convert_literal',
         ('0..n', 'list', '0..n', 'object'): 'convert_object',
         ('0..n', 'list', '0..n', 'voc'): 'convert_voc',
         ('0..n', 'list', '1', 'list'): 'convert_list',
         ('0..n', 'list', '1', 'literal'): 'convert_literal',
         ('0..n', 'list', '1', 'object'): 'convert_object',
         ('0..n', 'list', '1', 'voc'): 'convert_voc',
         ('0..n', 'list', '1..n', 'list'): 'convert_list',
         ('0..n', 'list', '1..n', 'literal'): 'convert_literal',
         ('0..n', 'list', '1..n', 'object'): 'convert_object',
         ('0..n', 'list', '1..n', 'voc'): 'convert_voc',
         ('0..n', 'list', 'n', 'list'): 'convert_list',
         ('0..n', 'list', 'n', 'literal'): 'convert_literal',
         ('0..n', 'list', 'n', 'object'): 'convert_object',
         ('0..n', 'list', 'n', 'voc'): 'convert_voc',
         ('0..n', 'literal', '0..1', 'list'): 'convert_list',
         ('0..n', 'literal', '0..1', 'literal'): 'convert_literal',
         ('0..n', 'literal', '0..1', 'object'): 'convert_object',
         ('0..n', 'literal', '0..1', 'voc'): 'convert_voc',
         ('0..n', 'literal', '0..n', 'list'): 'convert_list',
         ('0..n', 'literal', '0..n', 'literal'): 'convert_literal',
         ('0..n', 'literal', '0..n', 'object'): 'convert_object',
         ('0..n', 'literal', '0..n', 'voc'): 'convert_voc',
         ('0..n', 'literal', '1', 'list'): 'convert_list',
         ('0..n', 'literal', '1', 'literal'): 'convert_literal',
         ('0..n', 'literal', '1', 'object'): 'convert_object',
         ('0..n', 'literal', '1', 'voc'): 'convert_voc',
         ('0..n', 'literal', '1..n', 'list'): 'convert_list',
         ('0..n', 'literal', '1..n', 'literal'): 'convert_literal',
         ('0..n', 'literal', '1..n', 'object'): 'convert_object',
         ('0..n', 'literal', '1..n', 'voc'): 'convert_voc',
         ('0..n', 'literal', 'n', 'list'): 'convert_list',
         ('0..n', 'literal', 'n', 'literal'): 'convert_literal',
         ('0..n', 'literal', 'n', 'object'): 'convert_object',
         ('0..n', 'literal', 'n', 'voc'): 'convert_voc',
         ('0..n', 'object', '0..1', 'list'): 'convert_list',
         ('0..n', 'object', '0..1', 'literal'): 'convert_literal',
         ('0..n', 'object', '0..1', 'object'): 'convert_object',
         ('0..n', 'object', '0..1', 'voc'): 'convert_voc',
         ('0..n', 'object', '0..n', 'list'): 'convert_list',
         ('0..n', 'object', '0..n', 'literal'): 'convert_literal',
         ('0..n', 'object', '0..n', 'object'): 'convert_object',
         ('0..n', 'object', '0..n', 'voc'): 'convert_voc',
         ('0..n', 'object', '1', 'list'): 'convert_list',
         ('0..n', 'object', '1', 'literal'): 'convert_literal',
         ('0..n', 'object', '1', 'object'): 'convert_object',
         ('0..n', 'object', '1', 'voc'): 'convert_voc',
         ('0..n', 'object', '1..n', 'list'): 'convert_list',
         ('0..n', 'object', '1..n', 'literal'): 'convert_literal',
         ('0..n', 'object', '1..n', 'object'): 'convert_object',
         ('0..n', 'object', '1..n', 'voc'): 'convert_voc',
         ('0..n', 'object', 'n', 'list'): 'convert_list',
         ('0..n', 'object', 'n', 'literal'): 'convert_literal',
         ('0..n', 'object', 'n', 'object'): 'convert_object',
         ('0..n', 'object', 'n', 'voc'): 'convert_voc',
         ('0..n', 'voc', '0..1', 'list'): 'convert_list',
         ('0..n', 'voc', '0..1', 'literal'): 'convert_literal',
         ('0..n', 'voc', '0..1', 'object'): 'convert_object',
         ('0..n', 'voc', '0..1', 'voc'): 'convert_voc',
         ('0..n', 'voc', '0..n', 'list'): 'convert_list',
         ('0..n', 'voc', '0..n', 'literal'): 'convert_literal',
         ('0..n', 'voc', '0..n', 'object'): 'convert_object',
         ('0..n', 'voc', '0..n', 'voc'): 'convert_voc',
         ('0..n', 'voc', '1', 'list'): 'convert_list',
         ('0..n', 'voc', '1', 'literal'): 'convert_literal',
         ('0..n', 'voc', '1', 'object'): 'convert_object',
         ('0..n', 'voc', '1', 'voc'): 'convert_voc',
         ('0..n', 'voc', '1..n', 'list'): 'convert_list',
         ('0..n', 'voc', '1..n', 'literal'): 'convert_literal',
         ('0..n', 'voc', '1..n', 'object'): 'convert_object',
         ('0..n', 'voc', '1..n', 'voc'): 'convert_voc',
         ('0..n', 'voc', 'n', 'list'): 'convert_list',
         ('0..n', 'voc', 'n', 'literal'): 'convert_literal',
         ('0..n', 'voc', 'n', 'object'): 'convert_object',
         ('0..n', 'voc', 'n', 'voc'): 'convert_voc',
         ('1', 'list', '0..1', 'list'): 'convert_list',
         ('1', 'list', '0..1', 'literal'): 'convert_literal',
         ('1', 'list', '0..1', 'object'): 'convert_object',
         ('1', 'list', '0..1', 'voc'): 'convert_voc',
         ('1', 'list', '0..n', 'list'): 'convert_list',
         ('1', 'list', '0..n', 'literal'): 'convert_literal',
         ('1', 'list', '0..n', 'object'): 'convert_object',
         ('1', 'list', '0..n', 'voc'): 'convert_voc',
         ('1', 'list', '1', 'list'): 'convert_list',
         ('1', 'list', '1', 'literal'): 'convert_literal',
         ('1', 'list', '1', 'object'): 'convert_object',
         ('1', 'list', '1', 'voc'): 'convert_voc',
         ('1', 'list', '1..n', 'list'): 'convert_list',
         ('1', 'list', '1..n', 'literal'): 'convert_literal',
         ('1', 'list', '1..n', 'object'): 'convert_object',
         ('1', 'list', '1..n', 'voc'): 'convert_voc',
         ('1', 'list', 'n', 'list'): 'convert_list',
         ('1', 'list', 'n', 'literal'): 'convert_literal',
         ('1', 'list', 'n', 'object'): 'convert_object',
         ('1', 'list', 'n', 'voc'): 'convert_voc',
         ('1', 'literal', '0..1', 'list'): 'convert_list',
         ('1', 'literal', '0..1', 'literal'): 'convert_literal',
         ('1', 'literal', '0..1', 'object'): 'convert_object',
         ('1', 'literal', '0..1', 'voc'): 'convert_voc',
         ('1', 'literal', '0..n', 'list'): 'convert_list',
         ('1', 'literal', '0..n', 'literal'): 'convert_literal',
         ('1', 'literal', '0..n', 'object'): 'convert_object',
         ('1', 'literal', '0..n', 'voc'): 'convert_voc',
         ('1', 'literal', '1', 'list'): 'convert_list',
         ('1', 'literal', '1', 'literal'): 'convert_literal',
         ('1', 'literal', '1', 'object'): 'convert_object',
         ('1', 'literal', '1', 'voc'): 'convert_voc',
         ('1', 'literal', '1..n', 'list'): 'convert_list',
         ('1', 'literal', '1..n', 'literal'): 'convert_literal',
         ('1', 'literal', '1..n', 'object'): 'convert_object',
         ('1', 'literal', '1..n', 'voc'): 'convert_voc',
         ('1', 'literal', 'n', 'list'): 'convert_list',
         ('1', 'literal', 'n', 'literal'): 'convert_literal',
         ('1', 'literal', 'n', 'object'): 'convert_object',
         ('1', 'literal', 'n', 'voc'): 'convert_voc',
         ('1', 'object', '0..1', 'list'): 'convert_list',
         ('1', 'object', '0..1', 'literal'): 'convert_literal',
         ('1', 'object', '0..1', 'object'): 'convert_object',
         ('1', 'object', '0..1', 'voc'): 'convert_voc',
         ('1', 'object', '0..n', 'list'): 'convert_list',
         ('1', 'object', '0..n', 'literal'): 'convert_literal',
         ('1', 'object', '0..n', 'object'): 'convert_object',
         ('1', 'object', '0..n', 'voc'): 'convert_voc',
         ('1', 'object', '1', 'list'): 'convert_list',
         ('1', 'object', '1', 'literal'): 'convert_literal',
         ('1', 'object', '1', 'object'): 'convert_object',
         ('1', 'object', '1', 'voc'): 'convert_voc',
         ('1', 'object', '1..n', 'list'): 'convert_list',
         ('1', 'object', '1..n', 'literal'): 'convert_literal',
         ('1', 'object', '1..n', 'object'): 'convert_object',
         ('1', 'object', '1..n', 'voc'): 'convert_voc',
         ('1', 'object', 'n', 'list'): 'convert_list',
         ('1', 'object', 'n', 'literal'): 'convert_literal',
         ('1', 'object', 'n', 'object'): 'convert_object',
         ('1', 'object', 'n', 'voc'): 'convert_voc',
         ('1', 'voc', '0..1', 'list'): 'convert_list',
         ('1', 'voc', '0..1', 'literal'): 'convert_literal',
         ('1', 'voc', '0..1', 'object'): 'convert_object',
         ('1', 'voc', '0..1', 'voc'): 'convert_voc',
         ('1', 'voc', '0..n', 'list'): 'convert_list',
         ('1', 'voc', '0..n', 'literal'): 'convert_literal',
         ('1', 'voc', '0..n', 'object'): 'convert_object',
         ('1', 'voc', '0..n', 'voc'): 'convert_voc',
         ('1', 'voc', '1', 'list'): 'convert_list',
         ('1', 'voc', '1', 'literal'): 'convert_literal',
         ('1', 'voc', '1', 'object'): 'convert_object',
         ('1', 'voc', '1', 'voc'): 'convert_voc',
         ('1', 'voc', '1..n', 'list'): 'convert_list',
         ('1', 'voc', '1..n', 'literal'): 'convert_literal',
         ('1', 'voc', '1..n', 'object'): 'convert_object',
         ('1', 'voc', '1..n', 'voc'): 'convert_voc',
         ('1', 'voc', 'n', 'list'): 'convert_list',
         ('1', 'voc', 'n', 'literal'): 'convert_literal',
         ('1', 'voc', 'n', 'object'): 'convert_object',
         ('1', 'voc', 'n', 'voc'): 'convert_voc',
         ('1..n', 'list', '0..1', 'list'): 'convert_list',
         ('1..n', 'list', '0..1', 'literal'): 'convert_literal',
         ('1..n', 'list', '0..1', 'object'): 'convert_object',
         ('1..n', 'list', '0..1', 'voc'): 'convert_voc',
         ('1..n', 'list', '0..n', 'list'): 'convert_list',
         ('1..n', 'list', '0..n', 'literal'): 'convert_literal',
         ('1..n', 'list', '0..n', 'object'): 'convert_object',
         ('1..n', 'list', '0..n', 'voc'): 'convert_voc',
         ('1..n', 'list', '1', 'list'): 'convert_list',
         ('1..n', 'list', '1', 'literal'): 'convert_literal',
         ('1..n', 'list', '1', 'object'): 'convert_object',
         ('1..n', 'list', '1', 'voc'): 'convert_voc',
         ('1..n', 'list', '1..n', 'list'): 'convert_list',
         ('1..n', 'list', '1..n', 'literal'): 'convert_literal',
         ('1..n', 'list', '1..n', 'object'): 'convert_object',
         ('1..n', 'list', '1..n', 'voc'): 'convert_voc',
         ('1..n', 'list', 'n', 'list'): 'convert_list',
         ('1..n', 'list', 'n', 'literal'): 'convert_literal',
         ('1..n', 'list', 'n', 'object'): 'convert_object',
         ('1..n', 'list', 'n', 'voc'): 'convert_voc',
         ('1..n', 'literal', '0..1', 'list'): 'convert_list',
         ('1..n', 'literal', '0..1', 'literal'): 'convert_literal',
         ('1..n', 'literal', '0..1', 'object'): 'convert_object',
         ('1..n', 'literal', '0..1', 'voc'): 'convert_voc',
         ('1..n', 'literal', '0..n', 'list'): 'convert_list',
         ('1..n', 'literal', '0..n', 'literal'): 'convert_literal',
         ('1..n', 'literal', '0..n', 'object'): 'convert_object',
         ('1..n', 'literal', '0..n', 'voc'): 'convert_voc',
         ('1..n', 'literal', '1', 'list'): 'convert_list',
         ('1..n', 'literal', '1', 'literal'): 'convert_literal',
         ('1..n', 'literal', '1', 'object'): 'convert_object',
         ('1..n', 'literal', '1', 'voc'): 'convert_voc',
         ('1..n', 'literal', '1..n', 'list'): 'convert_list',
         ('1..n', 'literal', '1..n', 'literal'): 'convert_literal',
         ('1..n', 'literal', '1..n', 'object'): 'convert_object',
         ('1..n', 'literal', '1..n', 'voc'): 'convert_voc',
         ('1..n', 'literal', 'n', 'list'): 'convert_list',
         ('1..n', 'literal', 'n', 'literal'): 'convert_literal',
         ('1..n', 'literal', 'n', 'object'): 'convert_object',
         ('1..n', 'literal', 'n', 'voc'): 'convert_voc',
         ('1..n', 'object', '0..1', 'list'): 'convert_list',
         ('1..n', 'object', '0..1', 'literal'): 'convert_literal',
         ('1..n', 'object', '0..1', 'object'): 'convert_object',
         ('1..n', 'object', '0..1', 'voc'): 'convert_voc',
         ('1..n', 'object', '0..n', 'list'): 'convert_list',
         ('1..n', 'object', '0..n', 'literal'): 'convert_literal',
         ('1..n', 'object', '0..n', 'object'): 'convert_object',
         ('1..n', 'object', '0..n', 'voc'): 'convert_voc',
         ('1..n', 'object', '1', 'list'): 'convert_list',
         ('1..n', 'object', '1', 'literal'): 'convert_literal',
         ('1..n', 'object', '1', 'object'): 'convert_object',
         ('1..n', 'object', '1', 'voc'): 'convert_voc',
         ('1..n', 'object', '1..n', 'list'): 'convert_list',
         ('1..n', 'object', '1..n', 'literal'): 'convert_literal',
         ('1..n', 'object', '1..n', 'object'): 'convert_object',
         ('1..n', 'object', '1..n', 'voc'): 'convert_voc',
         ('1..n', 'object', 'n', 'list'): 'convert_list',
         ('1..n', 'object', 'n', 'literal'): 'convert_literal',
         ('1..n', 'object', 'n', 'object'): 'convert_object',
         ('1..n', 'object', 'n', 'voc'): 'convert_voc',
         ('1..n', 'voc', '0..1', 'list'): 'convert_list',
         ('1..n', 'voc', '0..1', 'literal'): 'convert_literal',
         ('1..n', 'voc', '0..1', 'object'): 'convert_object',
         ('1..n', 'voc', '0..1', 'voc'): 'convert_voc',
         ('1..n', 'voc', '0..n', 'list'): 'convert_list',
         ('1..n', 'voc', '0..n', 'literal'): 'convert_literal',
         ('1..n', 'voc', '0..n', 'object'): 'convert_object',
         ('1..n', 'voc', '0..n', 'voc'): 'convert_voc',
         ('1..n', 'voc', '1', 'list'): 'convert_list',
         ('1..n', 'voc', '1', 'literal'): 'convert_literal',
         ('1..n', 'voc', '1', 'object'): 'convert_object',
         ('1..n', 'voc', '1', 'voc'): 'convert_voc',
         ('1..n', 'voc', '1..n', 'list'): 'convert_list',
         ('1..n', 'voc', '1..n', 'literal'): 'convert_literal',
         ('1..n', 'voc', '1..n', 'object'): 'convert_object',
         ('1..n', 'voc', '1..n', 'voc'): 'convert_voc',
         ('1..n', 'voc', 'n', 'list'): 'convert_list',
         ('1..n', 'voc', 'n', 'literal'): 'convert_literal',
         ('1..n', 'voc', 'n', 'object'): 'convert_object',
         ('1..n', 'voc', 'n', 'voc'): 'convert_voc',
         ('n', 'list', '0..1', 'list'): 'convert_list',
         ('n', 'list', '0..1', 'literal'): 'convert_literal',
         ('n', 'list', '0..1', 'object'): 'convert_object',
         ('n', 'list', '0..1', 'voc'): 'convert_voc',
         ('n', 'list', '0..n', 'list'): 'convert_list',
         ('n', 'list', '0..n', 'literal'): 'convert_literal',
         ('n', 'list', '0..n', 'object'): 'convert_object',
         ('n', 'list', '0..n', 'voc'): 'convert_voc',
         ('n', 'list', '1', 'list'): 'convert_list',
         ('n', 'list', '1', 'literal'): 'convert_literal',
         ('n', 'list', '1', 'object'): 'convert_object',
         ('n', 'list', '1', 'voc'): 'convert_voc',
         ('n', 'list', '1..n', 'list'): 'convert_list',
         ('n', 'list', '1..n', 'literal'): 'convert_literal',
         ('n', 'list', '1..n', 'object'): 'convert_object',
         ('n', 'list', '1..n', 'voc'): 'convert_voc',
         ('n', 'list', 'n', 'list'): 'convert_list',
         ('n', 'list', 'n', 'literal'): 'convert_literal',
         ('n', 'list', 'n', 'object'): 'convert_object',
         ('n', 'list', 'n', 'voc'): 'convert_voc',
         ('n', 'literal', '0..1', 'list'): 'convert_list',
         ('n', 'literal', '0..1', 'literal'): 'convert_literal',
         ('n', 'literal', '0..1', 'object'): 'convert_object',
         ('n', 'literal', '0..1', 'voc'): 'convert_voc',
         ('n', 'literal', '0..n', 'list'): 'convert_list',
         ('n', 'literal', '0..n', 'literal'): 'convert_literal',
         ('n', 'literal', '0..n', 'object'): 'convert_object',
         ('n', 'literal', '0..n', 'voc'): 'convert_voc',
         ('n', 'literal', '1', 'list'): 'convert_list',
         ('n', 'literal', '1', 'literal'): 'convert_literal',
         ('n', 'literal', '1', 'object'): 'convert_object',
         ('n', 'literal', '1', 'voc'): 'convert_voc',
         ('n', 'literal', '1..n', 'list'): 'convert_list',
         ('n', 'literal', '1..n', 'literal'): 'convert_literal',
         ('n', 'literal', '1..n', 'object'): 'convert_object',
         ('n', 'literal', '1..n', 'voc'): 'convert_voc',
         ('n', 'literal', 'n', 'list'): 'convert_list',
         ('n', 'literal', 'n', 'literal'): 'convert_literal',
         ('n', 'literal', 'n', 'object'): 'convert_object',
         ('n', 'literal', 'n', 'voc'): 'convert_voc',
         ('n', 'object', '0..1', 'list'): 'convert_list',
         ('n', 'object', '0..1', 'literal'): 'convert_literal',
         ('n', 'object', '0..1', 'object'): 'convert_object',
         ('n', 'object', '0..1', 'voc'): 'convert_voc',
         ('n', 'object', '0..n', 'list'): 'convert_list',
         ('n', 'object', '0..n', 'literal'): 'convert_literal',
         ('n', 'object', '0..n', 'object'): 'convert_object',
         ('n', 'object', '0..n', 'voc'): 'convert_voc',
         ('n', 'object', '1', 'list'): 'convert_list',
         ('n', 'object', '1', 'literal'): 'convert_literal',
         ('n', 'object', '1', 'object'): 'convert_object',
         ('n', 'object', '1', 'voc'): 'convert_voc',
         ('n', 'object', '1..n', 'list'): 'convert_list',
         ('n', 'object', '1..n', 'literal'): 'convert_literal',
         ('n', 'object', '1..n', 'object'): 'convert',
         ('n', 'object', '1..n', 'voc'): 'convert_voc',
         ('n', 'object', 'n', 'list'): 'convert_list',
         ('n', 'object', 'n', 'literal'): 'convert_literal',
         ('n', 'object', 'n', 'object'): 'convert_object',
         ('n', 'object', 'n', 'voc'): 'convert_voc',
         ('n', 'voc', '0..1', 'list'): 'convert_list',
         ('n', 'voc', '0..1', 'literal'): 'convert_literal',
         ('n', 'voc', '0..1', 'object'): 'convert_object',
         ('n', 'voc', '0..1', 'voc'): 'convert_voc',
         ('n', 'voc', '0..n', 'list'): 'convert_list',
         ('n', 'voc', '0..n', 'literal'): 'convert_literal',
         ('n', 'voc', '0..n', 'object'): 'convert_object',
         ('n', 'voc', '0..n', 'voc'): 'convert_voc',
         ('n', 'voc', '1', 'list'): 'convert_list',
         ('n', 'voc', '1', 'literal'): 'convert_literal',
         ('n', 'voc', '1', 'object'): 'convert_object',
         ('n', 'voc', '1', 'voc'): 'convert_voc',
         ('n', 'voc', '1..n', 'list'): 'convert_list',
         ('n', 'voc', '1..n', 'literal'): 'convert_literal',
         ('n', 'voc', '1..n', 'object'): 'convert_object',
         ('n', 'voc', '1..n', 'voc'): 'convert_voc',
         ('n', 'voc', 'n', 'list'): 'convert_list',
         ('n', 'voc', 'n', 'literal'): 'convert_literal',
         ('n', 'voc', 'n', 'object'): 'convert_object',
         ('n', 'voc', 'n', 'voc'): 'convert_voc'
     }
    return solver[(of.subject_cardinality, of.subject_type, of.object_cardinality, of.object_type)]
