import sys
from lxml import etree, objectify

"""
class: admXML
For generating ADM XML using objectify
""" 

class admXML(object):   
    def __init__(self):
        """
        Class initialiser. Sets up bare ADM document
        """

        # Read in schema for validation
        fschema = open('data/adm_v3_itu.xsd', 'r')
        #self.schema = etree.XMLSchema(file=fschema)
        
        # Set up namespaces
        nsmaps = {None : "urn:metadata-schema:adm", 'xsi' : "http://www.w3.org/2001/XMLSchema-instance"}   
        nsxsi_e = objectify.ElementMaker(annotate=False, namespace=nsmaps['xsi'], nsmap=nsmaps)
        nsadm_e = objectify.ElementMaker(annotate=False, namespace=nsmaps[None], nsmap=nsmaps)

        # Set root of XML
        self.root = nsadm_e.ituADM()
        
        # We're diving down to audioFormatExtended
        self.ituADM = objectify.SubElement(self.root, "coreMetadata")
        self.coreMetadata = objectify.SubElement(self.ituADM, "format")
        self.audioFormatExtended = objectify.SubElement(self.coreMetadata, "audioFormatExtended")

        
    def Write(self, fxml):
        """
        Write out XML to a file
        """
        etree.strip_attributes(self.root, '{http://codespeak.net/lxml/objectify/pytype}pytype')
        objectify.deannotate(self.root, xsi_nil=True)
        etree.cleanup_namespaces(self.root)
        print(etree.tostring(self.root, pretty_print=True, xml_declaration=True, encoding='utf-8').decode(), file=fxml)


    def SetAudioProgramme(self, p_id, name, lang, start, end, cont_list, loudness):
        """
        Set audioProgramme element metadata
        """
        self.audioProgramme = objectify.SubElement(self.audioFormatExtended, "audioProgramme")
        self.audioProgramme.attrib['audioProgrammeID'] = p_id
        self.audioProgramme.attrib['audioProgrammeName'] = name
        if lang:       
            self.audioProgramme.attrib['audioProgrammeLanguage'] = lang
        if start:       
            self.audioProgramme.attrib['start'] = str(start)
        if end:       
            self.audioProgramme.attrib['end'] = str(end)
        if cont_list:
            for cont in cont_list:
                self.audioProgramme.append(objectify.Element("audioContentIDRef"))
                self.audioProgramme.audioContentIDRef[-1] = cont
        if loudness:
            self.audioProgramme.append(objectify.Element("loudness"))
            if 'integratedLoudness' in loudness:
                self.audioProgramme.loudness.integratedLoudness = str(loudness['integratedLoudness'])
            if 'loudnessRange' in loudness:
                self.audioProgramme.loudness.loudnessRange = str(loudness['loudnessRange'])
            if 'maxTruePeak' in loudness:
                self.audioProgramme.loudness.maxTruePeak = str(loudness['maxTruePeak'])
            if 'maxMomentary' in loudness:
                self.audioProgramme.loudness.maxMomentary = str(loudness['maxMomentary'])
            if 'maxShortTerm' in loudness:
                self.audioProgramme.loudness.maxShortTerm = str(loudness['maxShortTerm'])


    def SetAudioContent(self, c_id, name, lang, dialogue, obj_list, loudness):
        """
        Set audioContent element metadata
        """
        self.audioContent = objectify.SubElement(self.audioFormatExtended, "audioContent")
        self.audioContent.attrib['audioContentID'] = c_id
        self.audioContent.attrib['audioContentName'] = name
        if lang:       
            self.audioContent.attrib['audioContentLanguage'] = lang
        if dialogue:       
            self.audioContent.attrib['dialogue'] = str(dialogue)
        if obj_list:
            for obj in obj_list:
                self.audioContent.append(objectify.Element("audioObjectIDRef"))
                self.audioContent.audioObjectIDRef[-1] = obj
        if loudness:
            self.audioContent.append(objectify.Element("loudness"))
            if 'integratedLoudness' in loudness:
                self.audioContent.loudness.integratedLoudness = str(loudness['integratedLoudness'])
            if 'loudnessRange' in loudness:
                self.audioContent.loudness.loudnessRange = str(loudness['loudnessRange'])
            if 'maxTruePeak' in loudness:
                self.audioContent.loudness.maxTruePeak = str(loudness['maxTruePeak'])
            if 'maxMomentary' in loudness:
                self.audioContent.loudness.maxMomentary = str(loudness['maxMomentary'])
            if 'maxShortTerm' in loudness:
                self.audioContent.loudness.maxShortTerm = str(loudness['maxShortTerm'])


    def SetAudioObject(self, o_id, name, pack, atu_list, obj_list, start=None, duration=None, dialogue=None, importance=None, interact=None):
        """ 
        Set audioObject element metadata
        """
        self.audioObject = objectify.SubElement(self.audioFormatExtended, "audioObject")
        self.audioObject.attrib['audioObjectID'] = o_id
        self.audioObject.attrib['audioObjectName'] = name
        if start:
            self.audioObject.attrib['start'] = start
        if duration:
            self.audioObject.attrib['duration'] = duration
        if dialogue:
            self.audioObject.attrib['dialogue'] = str(dialogue)
        if importance:
            self.audioObject.attrib['importance'] = str(importance)
        if interact:
            self.audioObject.attrib['interact'] = str(interact)
        if pack:
            self.audioObject.append(objectify.Element("audioPackFormatIDRef"))
            self.audioObject.audioPackFormatIDRef[-1] = pack
        if atu_list:
            for atu in atu_list:
                self.audioObject.append(objectify.Element("audioTrackUIDRef"))
                self.audioObject.audioTrackUIDRef[-1] = atu
        if obj_list:
            for obj in obj_list:
                self.audioObject.append(objectify.Element("audioObjectIDRef"))
                self.audioObject.audioObjectIDRef[-1] = obj       


    def SetAudioPackFormat(self, p_id, name, chan_list, pack_list, typeLabel, typeDefinition, importance=None, abs_distance=None):
        """
        Set audioPackFormat element metadata
        """
        self.audioPackFormat = objectify.SubElement(self.audioFormatExtended, "audioPackFormat")  
        self.audioPackFormat.attrib['audioPackFormatID'] = p_id
        self.audioPackFormat.attrib['audioPackFormatName'] = name
        if typeLabel:
            self.audioPackFormat.attrib['typeLabel'] = str(typeLabel)
        if typeDefinition:
            self.audioPackFormat.attrib['typeDefinition'] = str(typeDefinition)
        if importance:
            self.audioPackFormat.attrib['importance'] = str(importance)
        if abs_distance:
            self.audioPackFormat.attrib['abs_distance'] = str(abs_distance)
        if chan_list:
            for chan in chan_list:
                self.audioPackFormat.append(objectify.Element("audioChannelFormatIDRef"))
                self.audioPackFormat.audioChannelFormatIDRef[-1] = chan                                
        if pack_list:
            for pack in pack_list:
                self.audioPackFormat.append(objectify.Element("audioPackFormatIDRef"))
                self.audioPackFormat.audioPackFormatIDRef[-1] = pack  


    def SetAudioChannelFormat(self, c_id, name, block_list, typeLabel, typeDefinition, frequency_h=None, frequency_l=None):
        """
        Set audioChannelFormat element metadata
        """
        self.audioChannelFormat = objectify.SubElement(self.audioFormatExtended, "audioChannelFormat")        
        self.audioChannelFormat.attrib['audioChannelFormatID'] = c_id
        self.audioChannelFormat.attrib['audioChannelFormatName'] = name
        if typeLabel:
            self.audioChannelFormat.attrib['typeLabel'] = str(typeLabel)
        if typeDefinition:
            self.audioChannelFormat.attrib['typeDefinition'] = str(typeDefinition)
        if frequency_h:
            self.audioChannelFormat.append(objectify.Element("frequency"))
            self.audioChannelFormat.frequency[-1] = frequency_h          
            self.audioChannelFormat.frequency[-1].attrib['typeDefinition'] = 'highPass'
        if frequency_l:
            self.audioChannelFormat.append(objectify.Element("frequency"))
            self.audioChannelFormat.frequency[-1] = frequency_l        
            self.audioChannelFormat.frequency[-1].attrib['typeDefinition'] = 'lowPass'
        if block_list:
            for block in block_list:
                self.SetAudioBlockFormat(self.audioChannelFormat, block, typeLabel, typeDefinition)
        else:
            self.audioBlockFormat = objectify.SubElement(self.audioChannelFormat, "audioBlockFormat")
            block_id = 'AB_' + c_id[3:11] + '_00000001'
            self.audioBlockFormat.attrib['audioBlockFormatID'] = block_id         


    def SetAudioBlockFormat(self, audioChannelFormat, block, typeLabel, typeDefinition):
        """
        Set audioBlockFormat element metadata
        """
        self.audioBlockFormat = objectify.SubElement(audioChannelFormat, "audioBlockFormat")
        self.audioBlockFormat.attrib['audioBlockFormatID'] = block['id']
        if 'rtime' in block:
            self.audioBlockFormat.attrib['rtime'] = block['rtime']
        if 'duration' in block:
            self.audioBlockFormat.attrib['duration'] = block['duration']
        if 'speakerLabel' in block:
            self.audioBlockFormat.append(objectify.Element("speakerLabel"))
            self.audioBlockFormat.speakerLabel[-1] = block['speakerLabel']
        if 'position' in block:
            is_cartesian = False
            for pos in block['position']:
                self.audioBlockFormat.append(objectify.Element("position"))
                self.audioBlockFormat.position[-1] = pos['value']
                if 'coordinate' in pos:
                    self.audioBlockFormat.position[-1].attrib['coordinate'] = pos['coordinate']
                    if pos['coordinate'] in ['X', 'Y', 'Z']:
                        is_cartesian = True
                if 'bound' in pos:
                    self.audioBlockFormat.position[-1].attrib['bound'] = pos['bound']
                if 'screenEdgeLock' in pos:
                    if pos['screenEdgeLock']:
                        self.audioBlockFormat.position[-1].attrib['screenEdgeLock'] = pos['screenEdgeLock']
            if is_cartesian:
                self.audioBlockFormat.append(objectify.Element("cartesian"))
                self.audioBlockFormat.cartesian[-1] = str(1)
        if 'matrix' in block:
            self.audioBlockFormat.append(objectify.Element("matrix"))
            for coef in block['matrix']:
                self.audioBlockFormat.matrix.append(objectify.Element("coefficient"))
                self.audioBlockFormat.matrix.coefficient[-1] = coef['idref']
                if 'gain' in coef:
                    self.audioBlockFormat.matrix.coefficient[-1].attrib['gain'] = str(coef['gain'])
                if 'gainVar' in coef:
                    self.audioBlockFormat.matrix.coefficient[-1].attrib['gainVar'] = coef['gainVar']
                if 'phase' in coef:
                    self.audioBlockFormat.matrix.coefficient[-1].attrib['phase'] = str(coef['phase'])
                if 'phaseVar' in coef:
                    self.audioBlockFormat.matrix.coefficient[-1].attrib['phaseVar'] = coef['phaseVar']
        if 'gain' in block:
            self.audioBlockFormat.append(objectify.Element("gain"))
            self.audioBlockFormat.gain[-1] = str(block['gain'])
        if 'diffuse' in block:
            self.audioBlockFormat.append(objectify.Element("diffuse"))
            self.audioBlockFormat.diffuse[-1] = str(block['diffuse'])
        if 'width' in block:
            self.audioBlockFormat.append(objectify.Element("width"))
            self.audioBlockFormat.width[-1] = str(block['width'])
        if 'height' in block:
            self.audioBlockFormat.append(objectify.Element("height"))
            self.audioBlockFormat.height[-1] = str(block['height'])
        if 'depth' in block:
            self.audioBlockFormat.append(objectify.Element("depth"))
            self.audioBlockFormat.depth[-1] = str(block['depth'])
        if 'channelLock' in block:
            self.audioBlockFormat.append(objectify.Element("channelLock"))
            self.audioBlockFormat.channelLock[-1] = str(block['channelLock'])
        if 'jumpPosition' in block:
            self.audioBlockFormat.append(objectify.Element("jumpPosition"))
            self.audioBlockFormat.jumpPosition[-1] = str(block['jumpPosition'])
        if 'equation' in block:
            self.audioBlockFormat.append(objectify.Element("equation"))
            self.audioBlockFormat.equation[-1] = str(block['equation'])
        if 'degree' in block:
            self.audioBlockFormat.append(objectify.Element("degree"))
            self.audioBlockFormat.degree[-1] = str(block['degree'])
        if 'order' in block:
            self.audioBlockFormat.append(objectify.Element("order"))
            self.audioBlockFormat.order[-1] = str(block['order'])
        if 'normalization' in block:
            self.audioBlockFormat.append(objectify.Element("normalization"))
            self.audioBlockFormat.normalization[-1] = str(block['normalization'])


    def SetAudioStreamFormat(self, s_id, name, track_list, channel, pack, formatLabel, formatDefinition):
        """
        Set audioStreamFormat element metadata
        """
        self.audioStreamFormat = objectify.SubElement(self.audioFormatExtended, "audioStreamFormat")
        self.audioStreamFormat.attrib['audioStreamFormatID'] = s_id
        self.audioStreamFormat.attrib['audioStreamFormatName'] = name
        if formatLabel:
            self.audioStreamFormat.attrib['formatLabel'] = str(formatLabel)
        if formatDefinition:
            self.audioStreamFormat.attrib['formatDefinition'] = str(formatDefinition)
        if channel:
            self.audioStreamFormat.append(objectify.Element("audioChannelFormatIDRef"))
            self.audioStreamFormat.audioChannelFormatIDRef[-1] = channel
        if pack:
            self.audioStreamFormat.append(objectify.Element("audioPackFormatIDRef"))
            self.audioStreamFormat.audioPackFormatIDRef[-1] = pack
        if track_list:
            for track in track_list:
                self.audioStreamFormat.append(objectify.Element("audioTrackFormatIDRef"))
                self.audioStreamFormat.audioTrackFormatIDRef[-1] = track


    def SetAudioTrackFormat(self, t_id, name, stream, formatLabel, formatDefinition):
        """
        Set audioTrackFormat element metadata
        """
        self.audioTrackFormat = objectify.SubElement(self.audioFormatExtended, "audioTrackFormat")
        self.audioTrackFormat.attrib['audioTrackFormatID'] = t_id
        self.audioTrackFormat.attrib['audioTrackFormatName'] = name
        if formatLabel:
            self.audioTrackFormat.attrib['formatLabel'] = str(formatLabel)
        if formatDefinition:
            self.audioTrackFormat.attrib['formatDefinition'] = str(formatDefinition)
        if stream:
            self.audioTrackFormat.append(objectify.Element("audioStreamFormatIDRef"))
            self.audioTrackFormat.audioStreamFormatIDRef[-1] = stream


    def SetAudioTrackUID(self, uid, sample_rate, bit_depth, mxf_lu=None, track_ref=None, pack_ref=None):
        """
        Set audioTrackUID element metadata 
        """
        self.audioTrackUID = objectify.SubElement(self.audioFormatExtended, "audioTrackUID")
        self.audioTrackUID.attrib['UID'] = uid
        if sample_rate:
            self.audioTrackUID.attrib['sampleRate'] = str(sample_rate)
        if bit_depth:
            self.audioTrackUID.attrib['bitDepth'] = str(bit_depth)
        if mxf_lu:
            self.audioTrackUID.append(objectify.Element("audioMXFLookUp"))
            if 'package' in mxf_lu:
                self.audioTrackUID.audioMXFLookUp.packageUIDRef = mxf_lu['package']
            if 'track' in mxf_lu:
                self.audioTrackUID.audioMXFLookUp.trackIDRef = mxf_lu['track']
            if 'channel' in mxf_lu:
                self.audioTrackUID.audioMXFLookUp.channelIDRef = mxf_lu['channel']
        if track_ref:
            self.audioTrackUID.audioTrackFormatIDRef = track_ref
        if pack_ref:    
            self.audioTrackUID.audioPackFormatIDRef = pack_ref
        
