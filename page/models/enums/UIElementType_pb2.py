# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: page/models/enums/UIElementType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='page/models/enums/UIElementType.proto',
  package='fkhp.page.layer.models.enums',
  syntax='proto3',
  serialized_options=_b('\n\034fkhp.page.layer.models.enumsP\001'),
  serialized_pb=_b('\n%page/models/enums/UIElementType.proto\x12\x1c\x66khp.page.layer.models.enums*\xc5\x17\n\rUIElementType\x12\x18\n\x14\x44\x45\x46\x41ULT_ELEMENT_TYPE\x10\x00\x12\r\n\tHELP_TEXT\x10\x01\x12\x13\n\x0f\x43REATIVE_IMAGES\x10\x02\x12\x12\n\x0e\x43REATIVE_IMAGE\x10\x03\x12\x13\n\x0fTITLE_CONTAINER\x10\x04\x12\t\n\x05TITLE\x10\x05\x12\r\n\tSUB_TITLE\x10\x06\x12\x13\n\x0fVIEW_ALL_BUTTON\x10\x07\x12\x0f\n\x0b\x42UTTON_TEXT\x10\x08\x12\x11\n\rPRODUCT_CARDS\x10\t\x12\x1a\n\x16PRODUCT_CARD_CONTAINER\x10\n\x12\x11\n\rPRODUCT_TITLE\x10\x0b\x12\x17\n\x13PRODUCT_FINAL_PRICE\x10\x0c\x12\x0f\n\x0bPRODUCT_MRP\x10\r\x12\x11\n\rPRODUCT_IMAGE\x10\x0e\x12\x10\n\x0cVALUE_MARKER\x10\x0f\x12\x0e\n\nADD_BUTTON\x10\x10\x12\x15\n\x11VALUE_MARKER_TEXT\x10\x11\x12\x13\n\x0f\x44ISCOUNT_MARKER\x10\x12\x12\x18\n\x14\x44ISCOUNT_MARKER_TEXT\x10\x13\x12\r\n\tMETA_TEXT\x10\x14\x12\x0e\n\nMETA_VALUE\x10\x15\x12\x0c\n\x08META_KEY\x10\x16\x12\x12\n\x0ePRODUCT_IMAGES\x10\x17\x12\x15\n\x11\x45LEMENT_CONTAINER\x10\x18\x12\n\n\x06\x42UTTON\x10\x19\x12\x16\n\x12PRODUCT_VARIATIONS\x10\x1a\x12 \n\x1cPRODUCT_VARIATIONS_CONTAINER\x10\x1b\x12\r\n\tRATE_CARD\x10\x1c\x12\x11\n\rDELIVERY_DATA\x10\x1d\x12\x15\n\x11\x41RTICLE_CONTAINER\x10\x1e\x12\x10\n\x0c\x41RTICLE_CARD\x10\x1f\x12\x0f\n\x0b\x44\x45SCRIPTION\x10 \x12\x0f\n\x0bSEARCH_ICON\x10!\x12\x10\n\x0cTOTAL_RATING\x10\"\x12\x0f\n\x0bRATING_META\x10#\x12\x17\n\x13RATING_DISTRIBUTION\x10$\x12\x0f\n\x0bRATING_CARD\x10%\x12\x0e\n\nRATING_KEY\x10&\x12\x10\n\x0cRATING_VALUE\x10\'\x12\x11\n\rELEMENT_IMAGE\x10(\x12\x0f\n\x0bRATING_ICON\x10)\x12\x12\n\x0eMULTIMEDIA_SET\x10*\x12\x1a\n\x16\x44\x45SCRIPTION_CONTAINERS\x10+\x12\x19\n\x15\x44\x45SCRIPTION_CONTAINER\x10,\x12\x0c\n\x08TEXT_BOX\x10-\x12\x10\n\x0cTEXT_ELEMENT\x10.\x12\x0f\n\x0b\x43ONTENT_URL\x10/\x12\x13\n\x0f\x41RROW_LEFT_ICON\x10\x30\x12\x0b\n\x07RX_ICON\x10\x31\x12\x10\n\x0cREORDER_ICON\x10\x32\x12\x0e\n\nADD_COUPON\x10\x33\x12\x12\n\x0e\x44ISPLAY_COUPON\x10\x34\x12\x0c\n\x08\x41\x44\x44_ICON\x10\x35\x12\x11\n\rDISCOUNT_ICON\x10\x36\x12\x0f\n\x0bRIGHT_ARROW\x10\x37\x12\x0e\n\nCLOSE_ICON\x10\x38\x12\x0e\n\nORDER_ICON\x10\x39\x12\x11\n\rLOCATION_ICON\x10:\x12\x0c\n\x08\x42OX_ICON\x10;\x12\x11\n\rQUESTION_ICON\x10<\x12\x10\n\x0cPREVIEW_ICON\x10=\x12\x0c\n\x08KEY_ICON\x10>\x12\x0f\n\x0bLOGOFF_ICON\x10?\x12\x10\n\x0c\x43OUPON_CARDS\x10@\x12\x14\n\x10\x43OUPON_CONTAINER\x10\x41\x12\x15\n\x11\x43OUPON_CARD_IMAGE\x10\x42\x12\x10\n\x0c\x43OUPON_IMAGE\x10\x43\x12\x11\n\rPAY_CASH_ICON\x10\x44\x12\x11\n\rPAYMENT_TYPES\x10\x45\x12\x10\n\x0cPAYMENT_TYPE\x10\x46\x12\x15\n\x11PAYMENT_CARD_ICON\x10G\x12\x16\n\x12PAYMENT_TYPE_IMAGE\x10H\x12\x0e\n\nBANK_NAMES\x10I\x12\x0e\n\nBACK_ARROW\x10J\x12\x11\n\rPAYMENT_CARDS\x10K\x12\r\n\tHOME_ICON\x10L\x12\r\n\tWORK_ICON\x10M\x12\x11\n\rADDRESS_CARDS\x10N\x12\x10\n\x0c\x41\x44\x44RESS_CARD\x10O\x12\x10\n\x0c\x41\x44\x44RESS_ICON\x10P\x12\x10\n\x0cPAYMENT_ICON\x10Q\x12\r\n\tMEDICINES\x10R\x12\x10\n\x0cORDERED_LIST\x10S\x12\x0c\n\x08\x43HECKBOX\x10T\x12\x0f\n\x0b\x43\x41MERA_ICON\x10U\x12\x13\n\x0fIMAGE_CONTAINER\x10V\x12\x10\n\x0cGALLERY_ICON\x10W\x12 \n\x1cPRESCRIPTION_CARDS_CONTAINER\x10X\x12\x1f\n\x1bPRESCRIPTION_CARD_CONTAINER\x10Y\x12\x16\n\x12PRESCRIPTION_CARDS\x10Z\x12\x10\n\x0cIMAGE_HOLDER\x10[\x12\x0e\n\nTRASH_ICON\x10\\\x12\x12\n\x0eIMAGE_SNAPSHOT\x10]\x12\x0c\n\x08\x44ROPDOWN\x10^\x12\x13\n\x0f\x44ROPDOWN_VALUES\x10_\x12\x17\n\x13HTML_RENDER_ELEMENT\x10`\x12\x12\n\x0e\x45LEMENT_HOLDER\x10\x61\x12\r\n\tMAPS_ICON\x10\x62\x12\x13\n\x0f\x44OWN_ARROW_ICON\x10\x63\x12\x0f\n\x0b\x43\x41NCEL_ICON\x10\x64\x12\x14\n\x10ORDER_INFO_CARDS\x10\x65\x12\x13\n\x0fORDER_INFO_CARD\x10\x66\x12\x18\n\x14ORDER_DELIVERED_ICON\x10g\x12\x15\n\x11ORDER_PACKED_ICON\x10h\x12\x16\n\x12ORDER_SHIPPED_ICON\x10i\x12\x18\n\x14ORDER_CONFIRMED_ICON\x10j\x12\x18\n\x14ORDER_CANCELLED_ICON\x10k\x12\x19\n\x15ORDER_DISPATCHED_ICON\x10l\x12\x13\n\x0fPAYMENT_DETAILS\x10m\x12\r\n\tEDIT_ICON\x10n\x12\x0f\n\x0bWALLET_ICON\x10o\x12\x11\n\rACCOUNT_CARDS\x10p\x12\x0e\n\nTRACK_ICON\x10q\x12\r\n\tFILE_ICON\x10r\x12\x16\n\x12\x42ULLETED_TEXT_LIST\x10s\x12\x11\n\rBULLETED_TEXT\x10t\x12\x0f\n\x0bRATING_DATA\x10u\x12\x16\n\x12RATING_COMPOSITION\x10v\x12\r\n\tCART_ICON\x10w\x12\x0f\n\x0bIMAGES_LIST\x10x\x12\x11\n\rARTICLE_CARDS\x10y\x12\x13\n\x0fTEXT_BOX_HOLDER\x10z\x12\x16\n\x12REASONS_RADIO_LIST\x10{\x12\x10\n\x0cRADIO_BUTTON\x10|\x12\x15\n\x11RADIO_BUTTON_TEXT\x10}\x12\x11\n\rBULLETED_LIST\x10~\x12\t\n\x05SALTS\x10\x7f\x12\x11\n\x0cGENERIC_INFO\x10\x80\x01\x12\x16\n\x11GENERIC_INFO_CARD\x10\x81\x01\x12\x0f\n\nTIMER_ICON\x10\x82\x01\x12\x0f\n\nCROSS_ICON\x10\x83\x01\x12\x0f\n\nSHARE_ICON\x10\x84\x01\x12\x15\n\x10NUMBER_CONTAINER\x10\x85\x01\x12\n\n\x05TIMER\x10\x86\x01\x12\x18\n\x13META_TEXT_CONTAINER\x10\x87\x01\x12\x17\n\x12SELLER_DETAIL_CARD\x10\x88\x01\x12\x1a\n\x15RELEVANT_SELLERS_LIST\x10\x89\x01\x12\x15\n\x10TEXT_BOX_ELEMENT\x10\x8a\x01\x12\x0f\n\nINFO_CARDS\x10\x8b\x01\x12\x10\n\x0bHEADER_TEXT\x10\x8c\x01\x12\x11\n\x0cWARNING_ICON\x10\x8d\x01\x12\x16\n\x11\x44\x45SCRIPTION_CARDS\x10\x8e\x01\x12\x17\n\x12\x44\x45SCRIPTION_HOLDER\x10\x8f\x01\x12#\n\x1ePRODUCT_AVAILABILITY_CONTAINER\x10\x90\x01\x12\x16\n\x11PRESCRIPTION_ICON\x10\x91\x01\x12\x11\n\x0c\x46ILTERS_LIST\x10\x92\x01\x12\x12\n\rFILTER_BUTTON\x10\x93\x01\x12\r\n\x08MIC_ICON\x10\x94\x01\x12\x12\n\rDOWNLOAD_ICON\x10\x95\x01\x12\r\n\x08\x46KH_LOGO\x10\x96\x01\x12\x10\n\x0b\x44\x45LETE_ICON\x10\x97\x01\x12\x13\n\x0eVIEW_FILE_ICON\x10\x98\x01\x42 \n\x1c\x66khp.page.layer.models.enumsP\x01\x62\x06proto3')
)

_UIELEMENTTYPE = _descriptor.EnumDescriptor(
  name='UIElementType',
  full_name='fkhp.page.layer.models.enums.UIElementType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_ELEMENT_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HELP_TEXT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_IMAGES', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREATIVE_IMAGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE_CONTAINER', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TITLE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUB_TITLE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEW_ALL_BUTTON', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUTTON_TEXT', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CARDS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_CARD_CONTAINER', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_TITLE', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_FINAL_PRICE', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_MRP', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_IMAGE', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_MARKER', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_BUTTON', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE_MARKER_TEXT', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOUNT_MARKER', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOUNT_MARKER_TEXT', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='META_TEXT', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='META_VALUE', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='META_KEY', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_IMAGES', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_CONTAINER', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUTTON', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_VARIATIONS', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_VARIATIONS_CONTAINER', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATE_CARD', index=28, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELIVERY_DATA', index=29, number=29,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE_CONTAINER', index=30, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE_CARD', index=31, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION', index=32, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEARCH_ICON', index=33, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TOTAL_RATING', index=34, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_META', index=35, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_DISTRIBUTION', index=36, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_CARD', index=37, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_KEY', index=38, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_VALUE', index=39, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_IMAGE', index=40, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_ICON', index=41, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MULTIMEDIA_SET', index=42, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_CONTAINERS', index=43, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_CONTAINER', index=44, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_BOX', index=45, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_ELEMENT', index=46, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONTENT_URL', index=47, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARROW_LEFT_ICON', index=48, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RX_ICON', index=49, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REORDER_ICON', index=50, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_COUPON', index=51, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISPLAY_COUPON', index=52, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADD_ICON', index=53, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DISCOUNT_ICON', index=54, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIGHT_ARROW', index=55, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE_ICON', index=56, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_ICON', index=57, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_ICON', index=58, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOX_ICON', index=59, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='QUESTION_ICON', index=60, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREVIEW_ICON', index=61, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KEY_ICON', index=62, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOGOFF_ICON', index=63, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUPON_CARDS', index=64, number=64,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUPON_CONTAINER', index=65, number=65,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUPON_CARD_IMAGE', index=66, number=66,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COUPON_IMAGE', index=67, number=67,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAY_CASH_ICON', index=68, number=68,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TYPES', index=69, number=69,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TYPE', index=70, number=70,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_CARD_ICON', index=71, number=71,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_TYPE_IMAGE', index=72, number=72,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BANK_NAMES', index=73, number=73,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BACK_ARROW', index=74, number=74,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_CARDS', index=75, number=75,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HOME_ICON', index=76, number=76,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WORK_ICON', index=77, number=77,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_CARDS', index=78, number=78,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_CARD', index=79, number=79,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADDRESS_ICON', index=80, number=80,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_ICON', index=81, number=81,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDICINES', index=82, number=82,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERED_LIST', index=83, number=83,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKBOX', index=84, number=84,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAMERA_ICON', index=85, number=85,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_CONTAINER', index=86, number=86,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GALLERY_ICON', index=87, number=87,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESCRIPTION_CARDS_CONTAINER', index=88, number=88,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESCRIPTION_CARD_CONTAINER', index=89, number=89,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESCRIPTION_CARDS', index=90, number=90,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_HOLDER', index=91, number=91,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRASH_ICON', index=92, number=92,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGE_SNAPSHOT', index=93, number=93,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROPDOWN', index=94, number=94,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DROPDOWN_VALUES', index=95, number=95,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HTML_RENDER_ELEMENT', index=96, number=96,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ELEMENT_HOLDER', index=97, number=97,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAPS_ICON', index=98, number=98,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWN_ARROW_ICON', index=99, number=99,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CANCEL_ICON', index=100, number=100,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_INFO_CARDS', index=101, number=101,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_INFO_CARD', index=102, number=102,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_DELIVERED_ICON', index=103, number=103,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_PACKED_ICON', index=104, number=104,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_SHIPPED_ICON', index=105, number=105,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_CONFIRMED_ICON', index=106, number=106,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_CANCELLED_ICON', index=107, number=107,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDER_DISPATCHED_ICON', index=108, number=108,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAYMENT_DETAILS', index=109, number=109,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EDIT_ICON', index=110, number=110,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WALLET_ICON', index=111, number=111,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_CARDS', index=112, number=112,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACK_ICON', index=113, number=113,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILE_ICON', index=114, number=114,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLETED_TEXT_LIST', index=115, number=115,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLETED_TEXT', index=116, number=116,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_DATA', index=117, number=117,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RATING_COMPOSITION', index=118, number=118,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CART_ICON', index=119, number=119,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMAGES_LIST', index=120, number=120,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ARTICLE_CARDS', index=121, number=121,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_BOX_HOLDER', index=122, number=122,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REASONS_RADIO_LIST', index=123, number=123,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADIO_BUTTON', index=124, number=124,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RADIO_BUTTON_TEXT', index=125, number=125,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BULLETED_LIST', index=126, number=126,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SALTS', index=127, number=127,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_INFO', index=128, number=128,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GENERIC_INFO_CARD', index=129, number=129,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMER_ICON', index=130, number=130,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CROSS_ICON', index=131, number=131,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHARE_ICON', index=132, number=132,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NUMBER_CONTAINER', index=133, number=133,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMER', index=134, number=134,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='META_TEXT_CONTAINER', index=135, number=135,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELLER_DETAIL_CARD', index=136, number=136,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELEVANT_SELLERS_LIST', index=137, number=137,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEXT_BOX_ELEMENT', index=138, number=138,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INFO_CARDS', index=139, number=139,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HEADER_TEXT', index=140, number=140,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING_ICON', index=141, number=141,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_CARDS', index=142, number=142,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DESCRIPTION_HOLDER', index=143, number=143,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRODUCT_AVAILABILITY_CONTAINER', index=144, number=144,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PRESCRIPTION_ICON', index=145, number=145,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTERS_LIST', index=146, number=146,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTER_BUTTON', index=147, number=147,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MIC_ICON', index=148, number=148,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOWNLOAD_ICON', index=149, number=149,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FKH_LOGO', index=150, number=150,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE_ICON', index=151, number=151,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VIEW_FILE_ICON', index=152, number=152,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=72,
  serialized_end=3085,
)
_sym_db.RegisterEnumDescriptor(_UIELEMENTTYPE)

UIElementType = enum_type_wrapper.EnumTypeWrapper(_UIELEMENTTYPE)
DEFAULT_ELEMENT_TYPE = 0
HELP_TEXT = 1
CREATIVE_IMAGES = 2
CREATIVE_IMAGE = 3
TITLE_CONTAINER = 4
TITLE = 5
SUB_TITLE = 6
VIEW_ALL_BUTTON = 7
BUTTON_TEXT = 8
PRODUCT_CARDS = 9
PRODUCT_CARD_CONTAINER = 10
PRODUCT_TITLE = 11
PRODUCT_FINAL_PRICE = 12
PRODUCT_MRP = 13
PRODUCT_IMAGE = 14
VALUE_MARKER = 15
ADD_BUTTON = 16
VALUE_MARKER_TEXT = 17
DISCOUNT_MARKER = 18
DISCOUNT_MARKER_TEXT = 19
META_TEXT = 20
META_VALUE = 21
META_KEY = 22
PRODUCT_IMAGES = 23
ELEMENT_CONTAINER = 24
BUTTON = 25
PRODUCT_VARIATIONS = 26
PRODUCT_VARIATIONS_CONTAINER = 27
RATE_CARD = 28
DELIVERY_DATA = 29
ARTICLE_CONTAINER = 30
ARTICLE_CARD = 31
DESCRIPTION = 32
SEARCH_ICON = 33
TOTAL_RATING = 34
RATING_META = 35
RATING_DISTRIBUTION = 36
RATING_CARD = 37
RATING_KEY = 38
RATING_VALUE = 39
ELEMENT_IMAGE = 40
RATING_ICON = 41
MULTIMEDIA_SET = 42
DESCRIPTION_CONTAINERS = 43
DESCRIPTION_CONTAINER = 44
TEXT_BOX = 45
TEXT_ELEMENT = 46
CONTENT_URL = 47
ARROW_LEFT_ICON = 48
RX_ICON = 49
REORDER_ICON = 50
ADD_COUPON = 51
DISPLAY_COUPON = 52
ADD_ICON = 53
DISCOUNT_ICON = 54
RIGHT_ARROW = 55
CLOSE_ICON = 56
ORDER_ICON = 57
LOCATION_ICON = 58
BOX_ICON = 59
QUESTION_ICON = 60
PREVIEW_ICON = 61
KEY_ICON = 62
LOGOFF_ICON = 63
COUPON_CARDS = 64
COUPON_CONTAINER = 65
COUPON_CARD_IMAGE = 66
COUPON_IMAGE = 67
PAY_CASH_ICON = 68
PAYMENT_TYPES = 69
PAYMENT_TYPE = 70
PAYMENT_CARD_ICON = 71
PAYMENT_TYPE_IMAGE = 72
BANK_NAMES = 73
BACK_ARROW = 74
PAYMENT_CARDS = 75
HOME_ICON = 76
WORK_ICON = 77
ADDRESS_CARDS = 78
ADDRESS_CARD = 79
ADDRESS_ICON = 80
PAYMENT_ICON = 81
MEDICINES = 82
ORDERED_LIST = 83
CHECKBOX = 84
CAMERA_ICON = 85
IMAGE_CONTAINER = 86
GALLERY_ICON = 87
PRESCRIPTION_CARDS_CONTAINER = 88
PRESCRIPTION_CARD_CONTAINER = 89
PRESCRIPTION_CARDS = 90
IMAGE_HOLDER = 91
TRASH_ICON = 92
IMAGE_SNAPSHOT = 93
DROPDOWN = 94
DROPDOWN_VALUES = 95
HTML_RENDER_ELEMENT = 96
ELEMENT_HOLDER = 97
MAPS_ICON = 98
DOWN_ARROW_ICON = 99
CANCEL_ICON = 100
ORDER_INFO_CARDS = 101
ORDER_INFO_CARD = 102
ORDER_DELIVERED_ICON = 103
ORDER_PACKED_ICON = 104
ORDER_SHIPPED_ICON = 105
ORDER_CONFIRMED_ICON = 106
ORDER_CANCELLED_ICON = 107
ORDER_DISPATCHED_ICON = 108
PAYMENT_DETAILS = 109
EDIT_ICON = 110
WALLET_ICON = 111
ACCOUNT_CARDS = 112
TRACK_ICON = 113
FILE_ICON = 114
BULLETED_TEXT_LIST = 115
BULLETED_TEXT = 116
RATING_DATA = 117
RATING_COMPOSITION = 118
CART_ICON = 119
IMAGES_LIST = 120
ARTICLE_CARDS = 121
TEXT_BOX_HOLDER = 122
REASONS_RADIO_LIST = 123
RADIO_BUTTON = 124
RADIO_BUTTON_TEXT = 125
BULLETED_LIST = 126
SALTS = 127
GENERIC_INFO = 128
GENERIC_INFO_CARD = 129
TIMER_ICON = 130
CROSS_ICON = 131
SHARE_ICON = 132
NUMBER_CONTAINER = 133
TIMER = 134
META_TEXT_CONTAINER = 135
SELLER_DETAIL_CARD = 136
RELEVANT_SELLERS_LIST = 137
TEXT_BOX_ELEMENT = 138
INFO_CARDS = 139
HEADER_TEXT = 140
WARNING_ICON = 141
DESCRIPTION_CARDS = 142
DESCRIPTION_HOLDER = 143
PRODUCT_AVAILABILITY_CONTAINER = 144
PRESCRIPTION_ICON = 145
FILTERS_LIST = 146
FILTER_BUTTON = 147
MIC_ICON = 148
DOWNLOAD_ICON = 149
FKH_LOGO = 150
DELETE_ICON = 151
VIEW_FILE_ICON = 152


DESCRIPTOR.enum_types_by_name['UIElementType'] = _UIELEMENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)